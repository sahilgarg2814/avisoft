import django.contrib.auth
import django.contrib.auth.forms
import django.contrib.auth.models
import django.shortcuts
import django.contrib.auth.decorators

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from tasks.forms import UserForm, UserProfileInfoForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task,UserProfileInfo,domain


def base_page(request):
    return render(request, 'base.html')


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo_list')
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid login credentials.'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register_page(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            profile = user_profile_form.save(commit=False)
            profile.user = user
            profile.save()
            # Redirect to a success page or another view after registration
            return redirect('login_page')
    else:
        user_form = UserForm()
        user_profile_form = UserProfileInfoForm()
    return render(request,'registration.html',{'user_form': user_form, 'user_profile_form': user_profile_form})



@login_required
def log_out(request):
    logout(request)
    return redirect('base')


@login_required
def todo_list(request):
    user_domain=request.user.userprofileinfo.domain.domain_name
    assigned_tasks=Task.objects.filter(to_which_user__domain=user_domain)
    context={
        'assigned_task':assigned_tasks
    }
    return render(request,'todo.html',context)















# Accessing related models through foreign keys:
# In Django models, when you have a ForeignKey field, it establishes a relationship between two models. 

# You can access related fields using dot notation.

# Retrieving the domain of the logged-in user:
# Given your models, UserProfileInfo has a ForeignKey field domain which points to the domain model.
# To retrieve the domain of the logged-in user, you would access it through the user's UserProfileInfo object.

# Correcting the access:
# Assuming that domain is indeed a ForeignKey field in the UserProfileInfo model pointing to the domain model, 
# and domain_name is a field in the domain model holding the actual domain name,

# Here's what each part means:

# request.user: This gives you the User object representing the currently logged-in user.
# userprofileinfo: This accesses the UserProfileInfo object associated with the logged-in user through the OneToOne relationship.
# domain: This accesses the domain object associated with the UserProfileInfo object through the ForeignKey relationship.
# domain_name: This accesses the domain_name field of the domain object, giving you the actual domain name.