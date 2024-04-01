from django.contrib import admin
from tasks.models import UserProfileInfo,domain,Task

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(domain)
admin.site.register(Task)