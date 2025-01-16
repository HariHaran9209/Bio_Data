#!/usr/bin/env bash


pip install -r requirements.txt
ls ./biodata
echo "Migrations starts"
python manage.py makemigrations
echo "Migrations Successfully Completed"
python manage.py migrate
echo "migrate Successfully Completed"
