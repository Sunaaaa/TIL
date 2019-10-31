from django.contrib import admin
from .models import Job

# Register your models here.

# 커스터 마이징한 ModelAdmin
class JobAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'past_job',)

admin.site.register(Job, JobAdmin)