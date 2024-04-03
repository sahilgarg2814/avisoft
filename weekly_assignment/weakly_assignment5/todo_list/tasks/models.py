from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfileInfo(models.Model):
    PYTHON = 'Python'
    MERN = 'Mern'
    JAVA = 'Java'
    DOMAIN_CHOICES = [
        (PYTHON, 'Python'),
        (MERN, 'Mern'),
        (JAVA, 'Java'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    domain=models.CharField(max_length=15,choices=DOMAIN_CHOICES)
    def __str__(self):
        return self.user.username

class Task(models.Model):
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

    PYTHON = 'Python'
    MERN = 'Mern'
    JAVA = 'Java'
    DOMAIN_CHOICES = [
        (PYTHON, 'Python'),
        (MERN, 'Mern'),
        (JAVA, 'Java'),
    ]

    task_number=models.AutoField(primary_key=True,validators=[MinValueValidator(1)])
    task_description=models.TextField(max_length=5000)
    status=models.CharField(max_length=1,choices=Status_Choices,default=Assigned)
    Assigned_time=models.DateTimeField(auto_now_add=True)
    domain=models.CharField(max_length=15,choices=DOMAIN_CHOICES)

    def __str__(self):
        return f"{self.task_number}+{self.task_description}"



@receiver(post_save, sender=Task)
def update_status(sender, instance, **kwargs):
    if instance.status == 'A' and timezone.now() > instance.Assigned_time + timezone.timedelta(minutes=30):
        instance.status = 'P'
        instance.save()
    elif instance.status == 'P' and timezone.now() > instance.Assigned_time + timezone.timedelta(hours=2):
        instance.status = 'M'
        instance.save()
    elif instance.status == 'C':
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





