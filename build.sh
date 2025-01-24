#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
echo 'Unapplying Migrations'
python manage.py migrate biodata zero
echo "Migrations starts"
python manage.py makemigrations biodata
echo "Migrations Successfully Completed"
python manage.py migrate biodata
echo "migrate Successfully Completed"
