from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50, null=False)
    slug=models.CharField(max_length=50, null=True, unique=True)
    description=models.TextField(null=False)
    price=models.IntegerField(null=False)
    discount=models.IntegerField(null=0, default=0)
    active=models.BooleanField(default=False)
    thumbnail=models.ImageField(upload_to="files/thumbnail")
    date=models.DateTimeField(auto_now_add=True)
    resource=models.ImageField(upload_to="files/resource")
    #length=models.IntegerField(null=False)

    def __str__(self):
        return self.name

class CourseProperty(models.Model):
    description=models.TextField(null=False)
    course=models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    class Meta :
        abstract = True

class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass

