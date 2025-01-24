#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
echo "Migrations starts"
python manage.py makemigrations
python manage.py makemigrations biodata
echo "Migrations Successfully Completed"
python manage.py migrate --fake-initial
echo "migrate Successfully Completed"
