from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.
class UserData(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('parent', 'Parent'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userdata_set',  # Changed related_name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userdata_permissions',  # Changed related_name to avoid conflict
        blank=True
    )

class BioData(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    address = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username}'s BioData"

class Index(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    studentname = models.CharField(max_length=100)
    dob = models.DateField()
    mothername = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    guardianname = models.CharField(max_length=100)
    aadharno = models.IntegerField()
    nameinaadhar = models.CharField(max_length=100)
    admissindate = models.DateField()
    address = models.CharField(max_length=250)
    pincode = models.IntegerField()
    phonenumber = models.IntegerField()
    alternatenumber = models.IntegerField()
    emailid = models.EmailField()
    BPL = models.CharField(max_length=100)
    AAY = models.CharField(max_length=100)
    EWS = models.BooleanField()
    CWSN = models.CharField(max_length=100)
    impairment = models.BooleanField()
    CWSN1 = models.BooleanField()
    disabilityparc = models.IntegerField()
    nationality = models.BooleanField()
    oosc = models.BooleanField()
    mainstream = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=100)
    admissionno = models.IntegerField()
    dateInput = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    subjects = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    marks = models.IntegerField()
    attendence = models.CharField(max_length=100)
    SLD = models.BooleanField()
    ASD = models.BooleanField()
    ADHD = models.BooleanField()
    special = models.BooleanField()
    sports = models.BooleanField()
    scouts = models.BooleanField()
    internet = models.BooleanField()
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    distance = models.CharField(max_length=100)
    quilification = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.studentname}'s BioData"

class Student(models.Model):
    name = models.CharField(max_length=125, null=True)
    age = models.IntegerField(null=True)
    admission_number = models.IntegerField(null=True)
    grade = models.CharField(max_length=10, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    dob = models.CharField(max_length=25, null=True)
    emailid = models.EmailField(null=True)
    stream = models.CharField(max_length=25, null=True)
    mother_name = models.CharField(max_length=125, null=True)
    father_name = models.CharField(max_length=125, null=True)
    aadhar_number = models.IntegerField(null=True)
    address = models.CharField(max_length=125, null=True)
    pincode = models.IntegerField(null=True)
    alt_phone_number = models.CharField(max_length=25, null=True)
    blood_group = models.CharField(max_length=15, null=True)
    height = models.CharField(max_length=15, null=True)
    weight = models.CharField(max_length=15, null=True)
    slug = models.SlugField(unique=True, blank=True)
    student_photo = models.ImageField(upload_to='student_photo/', default='student_photo/default.jpg')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.admission_number)
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class CustomUserModel(models.Model):
    username = models.CharField(max_length=125)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    name = models.CharField(max_length=125)
