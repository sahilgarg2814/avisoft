import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.settings')
django.setup()
from tasks.models import Task, UserProfileInfo, domain
from django.contrib.auth.models import User

# Delete data from custom models
Task.objects.all().delete()
UserProfileInfo.objects.all().delete()
domain.objects.all().delete()

# Delete data from the User model
User.objects.all().delete()