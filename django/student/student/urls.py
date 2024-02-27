"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_row/',views.create_row,name='create_row'),
    path('list_row/',views.list_rows,name='list_row'),
    path('<id>',views.detail_row),
    path('<id>/update',views.update_row,name='update_row'),
    path('<id>/delete',views.delete_row,name='delete_row')
]



# In Django's URL patterns, using <id> is a placeholder notation indicating that this part of the URL 
# should match any value and that value should be captured and passed to the associated view function.

# Here's why <id> is written as <id>:

# Placeholder: <id> acts as a placeholder in the URL pattern. It indicates that this part of the 
# URL can be replaced by any value. For example, if your URL pattern is path('<id>', views.detail_row), 
# then '<id>' can match any string