from django.db import models
class Students_model(models.Model):
    student_Name=models.CharField(max_length=264)
    student_Roll=models.IntegerField(primary_key=True)
    student_domain=models.CharField(max_length=264)

    def __str__(self):
        return str(self.student_Roll)