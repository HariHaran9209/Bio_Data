# Generated by Django 5.1.6 on 2025-02-09 08:08

from django.db import migrations, models
import django.utils.text
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='studentdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('age', models.IntegerField()),
                ('admission_number', models.IntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('grade', models.IntegerField()),
                ('dob', models.DateField()),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('emailid', models.EmailField(null=True, max_length=254)),
                ('stream', models.CharField(null=True, max_length=25)),
                ('mother_name', models.CharField(null=True, max_length=125)),
                ('father_name', models.CharField(null=True, max_length=125)),
                ('aadhar_number', models.IntegerField(null=True)),
                ('address', models.CharField(null=True, max_length=125)),
                ('pincode', models.IntegerField(null=True)),
                ('alt_phone_number', models.CharField(null=True, max_length=25)),
                ('blood_group', models.CharField(null=True, max_length=15)),
                ('height', models.CharField(null=True, max_length=15)),
                ('weight', models.CharField(null=True, max_length=15)),
                ('student_photo', models.ImageField(upload_to='student_photo/', default='student_photo/default.jpg')),
            ],
        ),
        migrations.CreateModel(
            name='teacherdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachername', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.User')),
            ],
        ),
    ]
