from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    pass

class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ["-id"]


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Course(models.Model):
    subject = models.CharField(max_length=255,null=False)
    description = models.TextField()
    image = models.ImageField(upload_to="course/%Y/%m/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['subject','category']

class Lesson(models.Model):
    subject = models.CharField(max_length=255,null=False)
    content = models.TextField(null=False)
    image = models.ImageField(upload_to="course/%Y/%m/")
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)

    def __str__(self):
        return self.subject