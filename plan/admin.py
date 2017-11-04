from django.contrib import admin
from .models import user_to_year, subject_info
from .models import school_info, school_subject, cls_info, topic, student
from .models import topic, unit, content
# Register your models here.
admin.site.register(user_to_year)
admin.site.register(subject_info)
admin.site.register(school_info)
admin.site.register(school_subject)
admin.site.register(cls_info)
admin.site.register(unit)
admin.site.register(topic)
admin.site.register(content)
admin.site.register(student)