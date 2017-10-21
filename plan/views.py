from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse 
from . import forms, models
from .models import initial_done, subject_info

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
		return render(request, 'plan/yearplan.html', {
			'step':1,
			'user': user})
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
		user = User.objects.get(username=usr)
		year = models.user_to_year(
			username = user,
			year_name = intro[0],
			term1_start=intro[1],
			term1_end=intro[2],
			term2_start=intro[3],
			term2_end=intro[4],
			term3_start=intro[5],
			term3_end=intro[6],
			term4_start=intro[7],
			term4_end=intro[8],
			)
		year.save()
		subject = subject_info.objects.all()
		return render(request, 'plan/yearplan.html', {
			'step':2,
			'sub': subject})
		#finally:
			# handle 404 error.
