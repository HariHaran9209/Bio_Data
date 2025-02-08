#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
echo "Flushing The Database"
python manage.py flush
echo "Migrations starts"
python manage.py makemigrations biodata
echo "Migrations Successfully Completed"
python manage.py migrate
echo "migrate Successfully Completed"
