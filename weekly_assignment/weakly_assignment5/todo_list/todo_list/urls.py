from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('my_admin/', admin.site.urls),
    path('', views.base_page, name='base'),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.log_out, name='log_out'),
    path('todo_list/',views.todo_list,name='todo_list')
]
