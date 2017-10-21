from django.contrib import admin
from .models import user_to_year, initial_done, subject_info
# Register your models here.
admin.site.register(user_to_year)
admin.site.register(initial_done)
admin.site.register(subject_info)