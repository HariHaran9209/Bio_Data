#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
echo "Migrations starts"
python manage.py makemigrations biodata
echo "Migrations Successfully Completed"
rm -rf biodata/migrations/*.py
python manage.py makemigrations biodata
python manage.py migrate biodata --fake
python manage.py migrate
echo "migrate Successfully Completed"
