from django.contrib.auth.models import AbstractBaseUser , BaseUser Manager, PermissionsMixin
from django.db import models
from django.utils.text import slugify

# Create your models here.
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
    
class CustomUser Manager(BaseUser Manager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser (AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUser Manager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Add any additional fields that are required for creating a user

    def __str__(self):
        return self.email
