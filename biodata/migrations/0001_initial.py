from django.db import migrations, models

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
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='teacherdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachername', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
