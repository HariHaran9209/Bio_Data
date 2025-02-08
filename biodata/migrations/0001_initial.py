from django.db import migrations, models
import django.utils.timezone
from django.utils.text import slugify

class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, null=True)),
                ('age', models.IntegerField(null=True)),
                ('admission_number', models.IntegerField(null=True)),
                ('grade', models.CharField(max_length=10, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('dob', models.CharField(max_length=25, null=True)),
                ('emailid', models.EmailField(null=True, max_length=254)),
                ('stream', models.CharField(max_length=25, null=True)),
                ('mother_name', models.CharField(max_length=125, null=True)),
                ('father_name', models.CharField(max_length=125, null=True)),
                ('aadhar_number', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=125, null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('alt_phone_number', models.CharField(max_length=25, null=True)),
                ('blood_group', models.CharField(max_length=15, null=True)),
                ('height', models.CharField(max_length=15, null=True)),
                ('weight', models.CharField(max_length=15, null=True)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('student_photo', models.ImageField(upload_to='student_photo/', default='student_photo/default.jpg')),
            ],
        ),
        migrations.CreateModel(
            name='customuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=125)),
                ('email', models.EmailField()),
                ('password', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=125)),
            ],
        ),
    ]
