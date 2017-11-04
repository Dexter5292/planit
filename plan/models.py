from django.db import models
from django.contrib.auth.models import User


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
	profile = models.ImageField('profile_pic', upload_to='./plan/static/plan/photos/')
	grade = models.CharField(max_length=5)
	subject = models.ForeignKey(subject_info, on_delete=models.CASCADE)

	def __str__(self):
		return self.class_name
	
	
	@property
	def filename(self):
		return os.path.basename(self.profile.name)

class unit(models.Model):
	subject = models.ForeignKey(subject_info, on_delete=models.CASCADE)
	unit_number = models.AutoField(primary_key=True)
	unit_name = models.CharField(max_length=100)
	syllabus = models.CharField(max_length=100)

	def __str__(self):
		return "Unit:  " + self.unit_name + "  [ " + self.subject.subject_name + " ]"

class topic(models.Model):
	unit = models.ForeignKey(unit, on_delete=models.CASCADE)
	topic_number = models.AutoField(primary_key=True)
	topic_name = models.CharField(max_length=300)

	def __str__(self):
		return "Topic: " + self.topic_name  

class content(models.Model):
	topic = models.ForeignKey(topic, on_delete=models.CASCADE)
	content_number = models.AutoField(primary_key=True)
	content_value = models.CharField(max_length=3000)

	def __str__(self):
		return "Content: " + str(self.content_number)

class student(models.Model):
	student_id = models.AutoField(primary_key=True)
	student_name = models.CharField(max_length=100)
	student_surname = models.CharField(max_length=100)
	student_gender = models.CharField(max_length=6)
	school_name = models.ForeignKey(school_info, on_delete=models.CASCADE)

