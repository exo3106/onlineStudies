from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

course_tabs = (
    ('about','ABOUT'),
    ('instructions','INSTRUCTIONS'),
    ('reviews','REVIEWS'),
    ('faq','FAQs'),
)
class Category(models.Model):
    name =  models.CharField(max_length=200)
    slug =  models.SlugField(max_length=200,unique=True)
        
    def __str__(self) -> str:
        return self.name

class Instructor(models.Model):
    instructor_name = models.ForeignKey(User,on_delete=models.CASCADE)
    about_instructors = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)

class Course(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    skills = models.CharField(max_length=100)
    univesity = models.CharField(max_length=100)
    instructor_id = models.ForeignKey(Instructor,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.course_name

class Video(models.Model):
    video_title = models.CharField(max_length=200)
    video_description = models.CharField(max_length=200)
    video_id = models.ForeignKey(Course,on_delete=models.CASCADE)

class Course_Module(models.Model):
    module_name = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    file = models.FileField()
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)

