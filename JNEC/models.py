from django.db import models

# Create your models here.

class Placed_Student(models.Model):
    First_Name = models.CharField(max_length = 50)
    Last_Name = models.CharField(max_length = 50)
    Department = models.CharField(max_length = 50)
    Company_Name = models.CharField(max_length = 50)
    Salary = models.IntegerField()

    def __str__(self):
        return f"{self.First_Name}"
    

    class Meta:
        db_table = "Placed_Student"

        
    