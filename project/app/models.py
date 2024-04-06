
from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_email = models.EmailField()
    stu_city = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'Student'
        verbose_name_plural = "Student" 
    
    def _str_(self):
        return self.stu_name