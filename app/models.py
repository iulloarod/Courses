from django.db import models


class CourseManager(models.Manager):
    def add_course_val(self, postData):
        errors ={}
        if len(postData['name']) < 5:
            errors['name'] = "Course Name should be at least 5 characters"
        if len(postData['description']) < 15 :
            errors['description'] = "Course description should be at least 15 characters"
        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    objects = CourseManager()