from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    age = models.IntegerField()
    email = models.EmailField()
    section = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
     return f"{self.first_name} {self.last_name}"
    
