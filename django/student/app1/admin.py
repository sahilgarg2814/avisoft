from django.contrib import admin

# Register your models here.
from app1.models import Students_model,movies_model
admin.site.register(Students_model)
admin.site.register(movies_model)