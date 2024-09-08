from django.db import models


class School(models.Model):
    full_name = models.CharField(max_length=255)
    abbreviated_name = models.CharField(max_length=50)
    address = models.TextField()
    
    def __str__(self) -> str:
        return self.full_name


class Classroom(models.Model):
    school = models.ForeignKey(
        School, 
        related_name='classrooms',
        on_delete=models.CASCADE
    )
    grade = models.PositiveIntegerField()
    section = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f"{self.grade} {self.section}"
    
    
class Teacher(models.Model):
    school = models.ForeignKey(
        School,
        related_name='teachers',
        on_delete=models.CASCADE
    )
    classroom = models.ManyToManyField(
        Classroom,
        related_name='teachers'
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    
class Student(models.Model):
    classroom = models.ForeignKey(
        Classroom, 
        related_name='students',
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"