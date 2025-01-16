#!/usr/bin/env bash


pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
echo "Migrations Successfully Completed"
