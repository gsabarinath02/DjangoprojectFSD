from django.db import models

# Create your models here.
class Degree(models.Model):
    title = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.title + ',' + self.branch

class Student(models.Model):
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=1)
    dob = models.DateTimeField('date of birth')

    def __str__(self):
        return self.roll_number + ',' + self.name #+ ',' + self.degree
