#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
echo "Showing Migrations"
python manage.py showmigrations
echo "Flushing The Database"
python manage.py flush --noinput
echo "Executing SQL Flush"
python manage.py sqlflush
echo "Migrations starts"
python manage.py makemigrations biodata
echo "Migrations Successfully Completed"
python manage.py migrate
echo "migrate Successfully Completed"
