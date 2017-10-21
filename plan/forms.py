from django import forms
from .models import user_to_year
from django.contrib.admin import widgets

class year_form(forms.ModelForm):
	
	datetest = forms.DateField(widget = widgets.AdminDateWidget)
	class Meta:	
		model = user_to_year
		fields = ['year_name', 'term1_start', 
		'term1_end', 'term2_start',
		'term2_end', 'term3_start',
		'term3_end', 'term4_start',
		'term4_end']
