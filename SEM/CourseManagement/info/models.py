from django.db import models
import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser):
    @property
    def is_student(self):
        if hasattr(self, 'student'):
            return True
        return False

    @property
    def is_teacher(self):
        if hasattr(self, 'teacher'):
            return True
        return False

    @property
    def is_admin(self):
        if hasattr(self, 'admin'):
            return True
        return False


gender_choice = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)

caste_choice = (
    ('OC', 'OC'),
    ('BC-A', 'BC-A'),
    ('BC-B', 'BC-B'),
    ('BC-C', 'BC-C'),
    ('BC-D', 'BC-D'),
    ('BC-E', 'BC-E'),
    ('SC', 'SC'),
    ('ST', 'ST'),

)

religion_choice = (
    ('Hindu', 'Hindu'),
    ('Christian', 'Christian'),
    ('Muslim', 'Muslim'),
    ('Sikh', 'Sikh'),
    ('Buddist', 'Buddist'),
)

test_name = (
    ('Mid test 1', 'Mid test 1'),    
    ('Mid test 2', 'Mid test 2'),
    ('Semester End Exam', 'Semester End Exam'),
)

ph_choice = (
    ('Yes', 'Yes'),
    ('No', 'No')

)

adm_cat_choice = (
    ('Convener Quota', 'Convener Quota'),
    ('Management Quota', 'Management Quota')
)


time_slots = (
    ('7:30 - 8:30', '7:30 - 8:30'),
    ('8:30 - 9:30', '8:30 - 9:30'),
    ('9:30 - 10:30', '9:30 - 10:30'),
    ('11:00 - 11:50', '11:00 - 11:50'),
    ('11:50 - 12:40', '11:50 - 12:40'),
    ('12:40 - 1:30', '12:40 - 1:30'),
    ('2:30 - 3:30', '2:30 - 3:30'),
    ('3:30 - 4:30', '3:30 - 4:30'),
    ('4:30 - 5:30', '4:30 - 5:30'),
)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    HTNo = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200, null=True)
    father_name = models.CharField(max_length= 200, null=True)
    college_code = models.CharField(max_length=5, null=True)
    Gender = models.CharField(max_length=50, choices=gender_choice, default='Male')
    phone_regex = RegexValidator(regex = '^\+?1?\d{10,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    reservation = models.CharField(max_length=5, choices=caste_choice, default = 'OC')
    DOB = models.DateField(default='1998-01-01')
    address = models.CharField(max_length=500, default='India')
    email = models.EmailField(max_length = 200)
    scribe = models.CharField(max_length=10, choices = ph_choice, default = 'No')
    religion = models.CharField(max_length=20, choices = religion_choice, default = 'Hindu')
    ph_status = models.CharField(max_length=5, choices = ph_choice, default = 'No')
    adhar_number = models.CharField(max_length=15, null=True)
    
    def __str__(self):
        return self.name



class Teacher(models.Model):
    id = models.CharField(primary_key='True', max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=50, choices=gender_choice, default='Male')
    DOB = models.DateField(default='1980-01-01')
    email = models.EmailField(max_length= 200)
    phone_regex = RegexValidator(regex = '^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)

    def __str__(self):
        return self.name

class Admin(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length= 100)
    Gender = models.CharField(max_length=10, choices=gender_choice, default='Male')
    DOB = models.DateField(default='1980-01-01')
    email = models.EmailField(max_length=200)
    phone_regex = RegexValidator(regex = '^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)

    def __str__(self):
        return self.name
