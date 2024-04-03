from django.contrib import admin
from tasks.models import UserProfileInfo,Task

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Task)