from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class studentdata(models.Model):
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
        super(studentdata, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class teacherdata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    teachername = models.CharField(max_length=125, null=False)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
