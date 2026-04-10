from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ExerciseSchedule(models.Model):
    relation=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Exercise_name=models.CharField(max_length=50)
    sets_reps=models.CharField(max_length=20)
    coach_notes=models.TextField(null=True)

    def __str__(self):
        return self.Exercise_name
    
class NutrationPlane(models.Model):
    relation=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    Meal=models.CharField(max_length=50)
    Food_items=models.CharField(max_length=50)
    Macros=models.CharField(max_length=50)
    time=models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.Meal


class video(models.Model):
    relation=models.ForeignKey(User, on_delete=models.CASCADE)
    desc=models.TextField(null=True)
    video=models.FileField( upload_to='doc/', max_length=100)

    def __str__(self):
        return self.desc