from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class domain(models.Model):
    domain_name=models.CharField(max_length=1000)

    def __str__(self):
        return self.domain_name

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # # Add any additional attributes you want
    # portfolio_site = models.URLField(blank=True)
    # # pip install pillow to use this!
    # # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    # def __str__(self):
    #     # Built-in attribute of django.contrib.auth.models.User !
    #     return self.user.username

    def __str__(self):
        return self.user.username
    
    @property
    def username(self):
        return self.user.username
    
    @property
    def password(self):
        return self.user.password
    
    @property
    def email(self):
        return self.user.email
    
    @property
    def first_name(self):
        return self.user.first_name
    
    @property
    def last_name(self):
        return self.user.last_name
    
    domain=models.ForeignKey(domain,on_delete=models.CASCADE)
    
    # These are properties (decorated with @property) that allow you 
    # to access the basic fields (username, password, email, first name, and last name) of 
    # the associated User object directly from an instance of YourCustomModel. 
    # Each property returns the corresponding field value of the associated User object

class task(models.Model):
    Assigned='A'
    Pending='P'
    Missed='M'
    Complete='C'
    Status_Choices=[
        (Assigned,'Assigned'),
        (Pending,'Pending'),
        (Missed,'Miseed'),
        (Complete,'Complete')
    ]
    task_number=models.IntegerField(primary_key=True,validators=[MinValueValidator(1)])
    task_description=models.TextField(max_length=5000)
    status=models.CharField(max_length=1,choices=Status_Choices,default=Assigned)
    Assigned_time=models.DateTimeField(auto_now_add=True)

    to_which_user=models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.task_number}+{self.task_description}"
    


@receiver(post_save, sender=task)
def update_status(sender, instance, **kwargs):
    if instance.status == task.Assigned and timezone.now() > instance.Assigned_time + timezone.timedelta(minutes=30):
        instance.status = task.Pending
        instance.save()
    elif instance.status == task.Pending and timezone.now() > instance.Assigned_time + timezone.timedelta(hours=2):
        instance.status = task.Missed
        instance.save()
    elif instance.status==task.Complete:
        pass
        


# The pre_save signal is sent just before a model's save() method is called. It allows you to perform actions or make
# modifications to the model instance just before it's saved to the database. For example, 
# you might use pre_save to automatically populate certain fields, validate data, or perform any necessary preprocessing.

# Here's a brief overview of how pre_save signal works:

# You define a function that will handle the pre_save signal for a specific model.
# You connect this function to the pre_save signal for the model using the @receiver decorator.
# When an instance of the model is about to be saved, the pre_save signal is emitted.
# Django calls the function connected to the pre_save signal for the model, passing the instance of the model as an argument.
# Inside the function, you can perform any necessary operations on the instance before it's saved to the database.
# post_save Signal:
# The post_save signal is sent just after a model's save() method is called and the model instance has been saved to the database.
# It allows you to perform actions or make modifications after the instance has been saved. For example, 
# you might use post_save to update related models, trigger notifications, or perform any post-processing tasks.

# Here's a brief overview of how post_save signal works:

# You define a function that will handle the post_save signal for a specific model.
# You connect this function to the post_save signal for the model using the @receiver decorator.
# When an instance of the model is saved and the post_save signal is emitted.
# Django calls the function connected to the post_save signal for the model, passing the instance of the model as an argument.
# Inside the function, you can perform any necessary operations on the instance after it has been saved to the database.
# In summary, pre_save allows you to intercept and modify the instance before it's saved, while post_save allows you to 
# perform actions after the instance has been saved. These signals are useful for implementing various types of functionality, 
# such as validation, preprocessing, and post-processing tasks.





