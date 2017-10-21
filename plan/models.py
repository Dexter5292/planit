from django.db import models
from django.contrib.auth.models import User

class initial_done(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	done = models.BooleanField(default=False)

class user_to_year(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	year_name = models.IntegerField()
	term1_start = models.DateField()
	term1_end = models.DateField()
	term2_start = models.DateField()
	term2_end = models.DateField()
	term3_start = models.DateField()
	term3_end = models.DateField()
	term4_start = models.DateField()
	term4_end = models.DateField()

class school_info(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	sch_name = models.CharField(max_length=300)
	sch_period_num = models.IntegerField()
	sch_period_length = models.IntegerField()

class subject_info(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	subject_code = models.CharField(max_length=10)
	subject_name = models.CharField(max_length=300)
	subject_level = models.CharField(max_length=4)

	def __str__(self):
		return self.subject_name