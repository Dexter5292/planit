from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse 
from . import forms, models, scedule,termsoup
from .models import subject_info, school_info, school_subject
from .models import student, cls_info


def dashboard(request, uname):
	user = User.objects.get(username=uname)
	subjects = subject_info.objects.filter(username=user)
	ppic = cls_info.objects.get(teacher=user)
	ppic = ppic.profile.name[4:]
	return render(request, 'plan/dashboard.html',
	{'user': user,
	 'subjects': subjects,
	 'profile_pic': ppic})


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
		subjects = subject_info.objects.filter(username=user)
		if user is not None: 
			# Login to Homepage,

			return redirect('./dashboard/%s/' % user.username, {
				'user': user,
				'subjects': subjects,
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
			'user': request.POST.get('usr_name'),
			'subject': sub,
			'school_name': intro[0]
			})
	elif step == '3':
		intro =[
		request.POST.get('rtotal'),      # 0
		request.POST.get('grade'),       # 1
		request.POST.get('Prac_Sub'),    # 2
		request.POST.get('prac_ratio'),  # 3
		request.POST.get('syllabus'),    # 4
		request.POST.get('usr_name'),    # 5
		request.POST.get('sch_name'),    # 6
		request.POST.get('subject')]     # 7
			# Load post to database
		if intro[2] == "Yes":
			boolvar = True
		else:
			boolvar = False
		user = User.objects.get(username=intro[5])
		school = school_info.objects.filter(sch_name=intro[6])
		school = school[0]
		subject = subject_info.objects.get(subject_name=intro[7])
		sch_sub = school_subject(
			school=school,
			user=user,
			subject=subject,
			periods=int(intro[0][0]),
			grade=intro[1],
			prac=boolvar,
			ratio=intro[3],
			syllabus=intro[4]
			)
		sch_sub.save()
			# Redirect to class_info 'optional'
			
		return render(request, 'plan/yearplan.html', {
			'step':4,
			'user': user.username,
			'subject': subject,
			'school_name': intro[6],
			'grade': intro[1]
			})
	elif step == '4':
		intro = [
		request.POST.get('cls_name'),
		request.POST.get('add_now'),
		request.POST.get('usr_name'),
		request.POST.get('sch_name'),
		request.POST.get('grade'),
		request.POST.get('subject')
		]

		if intro[1] == "Yes":
			user = User.objects.get(username=intro[2])
			return render(request, 'plan/yearplan.html', {
			'step':5,
			'user': user,
			'subject': intro[5],
			'school_name': intro[3],
			'grade': intro[4]})
	elif step == '5':
		intro = [
		request.POST.get('subject'),
		request.POST.get('sch_name'),
		request.POST.get('grade'),
		request.POST.get('usr_name'),
		request.POST.get('counter'),
		request.FILES.get('profilepic'),
		request.POST.get('cls_name')
		]
		school__name = school_info.objects.filter(sch_name=intro[1])
		Class__name = intro[6]
		user = User.objects.filter(username=intro[3])
		user = user[0]
		profilepic = intro[5]
		grade = intro[2]
		subject__name = subject_info.objects.filter(subject_name=intro[1])
		subject__name = subject__name[0]

		this_class = cls_info.objects.create(school=school__name,
			class_name=Class__name,
			teacher=user,
			profile=profilepic,
			grade=grade,
			subject=subject__name)
		this_class.save()
		studs = ["","",""]
		for i in range(1, int(intro[4]) + 1):
			names =(request.POST.get("%s_getName" % i))
			surns = (request.POST.get("%s_getSurname" % i))
			gender = (request.POST.get("%s_gender" % i))
			studs[0] = names
			studs[1] = surns
			studs[2] = gender
			schoolName = school_info.objects.filter(sch_name=intro[1])
			schoolName = schoolName[0]
			tstudent = student(student_name=names,
				student_surname=surns,
				student_gender=gender,
				school_name=schoolName
				)
			tstudent.save()
			username = intro[3]
		return redirect('/dashboard/%s/' % username)
		#finally:
			# handle 404 error.

def planit(request, uname):
	return render(request, 'plan/planit.html', {
		'user':uname,
		'step': '0'})