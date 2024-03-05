from django.db import models

# model baesd on students records
class Students_model(models.Model):
    student_Name=models.CharField(max_length=264)  
    student_Roll=models.IntegerField(primary_key=True)
    student_domain=models.CharField(max_length=264)

    def __str__(self):
        return str(self.student_Roll)

class movies_model(models.Model):
    movie_name=models.CharField(max_length=50,primary_key=True)
    movie_description=models.CharField(max_length=200)
    movie_active=models.BooleanField(default=True)

    def __str__(self):
        return self.movie_name