from django.contrib import admin
from course.models import Category, Course, Lesson
# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)