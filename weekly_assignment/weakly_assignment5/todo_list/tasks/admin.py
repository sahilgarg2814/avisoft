from django.contrib import admin
from tasks.models import UserProfileInfo,domain,task

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(domain)
admin.site.register(task)