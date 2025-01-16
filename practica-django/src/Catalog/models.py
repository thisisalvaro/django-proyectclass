from django.db import models

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()
    teacher = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    
    def __str__(self):
        return f"Nombre : {self.name} Email: {self.email}"