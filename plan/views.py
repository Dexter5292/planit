from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse 
from . import forms, models, scedule,termsoup
from .models import initial_done, subject_info, school_info

def home(request):
	if request.method == "GET":
		# Render login screen.
		return render(request, 'plan/home.html')
	else:
		# Authenticate user on form submission via POST
		# get POST cridentials.
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(username=email, password=password)
		if user is not None: 
			# Login to Homepage,

			return render(request, 'plan/user_page.html', {
				'user': user,
				})
		else:
			# Retry / Register,
			failed = True
			return render(request, 'plan/home.html', {
				'failed': failed
				})


def register(request):
	if request.method == 'GET':
		# This code will execute on first load.

		return render(request, 'plan/register.html')
	else:
		# This will be selected on form submission.

		# Retrieve user info for submission into django 
		# user table.

		user_name = request.POST.get('username')
		password = request.POST.get('password')
		email = user_name
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')

		# Load to database:

		user = User.objects.create_user(username=user_name)
		user.password = password
		user.email = email
		user.first_name = firstname
		user.last_name = lastname
		user.save()

		setup = initial_done.objects.create(username=user)
		setup.save()

		return render(request, 'plan/setup.html',
			{
			'user': user
			})

def yearplan(request):
	step = request.POST.get('step')
	if step == '0':
		user = User.objects.get(username=request.POST.get('usr_name'))
		dept_suggest = termsoup.department_recommendations()
		t1 = dept_suggest[0]
		t2 = dept_suggest[1]
		t3 = dept_suggest[2]
		t4 = dept_suggest[3]
		return render(request, 'plan/yearplan.html', {
			'step':1,
			'user': user,
			"term1_date": t1,
			"term2_date": t2,
			"term3_date": t3,
			"term4_date": t4})
	elif step == '1':
		# Handle input to db
		intro = [request.POST.get('year_name'),
		request.POST.get('t1s'),
		request.POST.get('t1e'),
		request.POST.get('t2s'),
		request.POST.get('t2e'),
		request.POST.get('t3s'),
		request.POST.get('t3e'),
		request.POST.get('t4s'),
		request.POST.get('t4e'),
		request.POST.get('step_hold')]
		usr = request.POST.get('usr_name')

		term1 = scedule.weekdays(intro[1], intro[2])
		term2 = scedule.weekdays(intro[3], intro[4])
		term3 = scedule.weekdays(intro[5], intro[6])
		term4 = scedule.weekdays(intro[7], intro[8])
		
		user = User.objects.get(username=usr)
		year = models.user_to_year(
			username = user,
			year_name= intro[0],
			term1_days=term1,
			term2_days=term2,
			term3_days=term3,
			term4_days=term4
			)
		year.save()
		subject = subject_info.objects.all()
		return render(request, 'plan/yearplan.html', {
			'step':2,
			'sub': subject,
			'user':user
			})
	elif step == '2':
		intro = [
		request.POST.get('sch_name'),
		request.POST.get('subject'),
		request.POST.get('period_time'),
		request.POST.get('table_span'),
		request.POST.get('step_hold'),
		]
		roster_len = int(intro[3][0])
		usr = request.POST.get('usr_name')
		usr = User.objects.get(username=usr)
		sub = subject_info.objects.get(subject_name=intro[1])
		school = school_info(username=usr,
			sch_name=intro[0],
			sch_table_span=roster_len,
			sch_period_length=intro[2]
			)
		school.save()
		return render(request, 'plan/yearplan.html', {
			'step':3,
			'user': usr,
			'subject': sub,
			'school_name': intro[0]
			})
	elif step == '3':

		# Load post to database
		# Redirect to class_info 'optional'
		
		return HttpResponse("Success")
		#finally:
			# handle 404 error.
