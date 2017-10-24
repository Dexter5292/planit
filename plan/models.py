from django.db import models
from django.contrib.auth.models import User

class initial_done(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	done = models.BooleanField(default=False)
	if done == True:
		state = "Completed"
	else:
		state = "No Completed"

	def __str__(self):
		return self.state

class user_to_year(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	year_name = models.IntegerField()
	term1_days = models.IntegerField()
	term2_days = models.IntegerField()
	term3_days = models.IntegerField()
	term4_days = models.IntegerField()

	def __str__(self):
		return  "Year saved: " + str(self.year_name)


class subject_info(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	subject_code = models.CharField(max_length=10)
	subject_name = models.CharField(max_length=300)
	subject_level = models.CharField(max_length=4)

	def __str__(self):
		return self.subject_name

class school_info(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	sch_name = models.CharField(max_length=300)
	sch_table_span = models.IntegerField(default=1)
	sch_period_length = models.IntegerField(default=30)

	def __str__(self):
		return "School:  " + self.sch_name

class school_subject(models.Model):
	school = models.ForeignKey(school_info, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	subject = models.ForeignKey(subject_info, on_delete=models.CASCADE)
	periods = models.IntegerField(default=4)
	grade = models.CharField(max_length=50)
	prac = models.BooleanField(default=False)
	ratio = models.CharField(max_length=20)
	syllabus = models.CharField(max_length=100)

class cls_info(models.Model):
	school = models.ForeignKey(school_info, on_delete=models.CASCADE)
	class_name = models.CharField(max_length=30)
	teacher = models.ForeignKey(User, on_delete=models.CASCADE)
	grade = models.CharField(max_length=5)
	subject = models.ForeignKey(subject_info, on_delete=models.CASCADE)

	def __str__(self):
		return self.class_name

class topics(models.Model):
	subject = models.ForeignKey(subject_info, on_delete=models.CASCADE)
	topic_number = models.AutoField(primary_key=True)
	topic_name = models.CharField(max_length=100)
	syllabus = models.CharField(max_length=100)

	def __str__(self):
		return "Topic:  " + self.topic_name + "  [ " + self.subject.subject_name + " ]"
