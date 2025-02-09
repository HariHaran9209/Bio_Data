#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

python manage.py makemigrations 
echo "Migrations Successfully Completed For b"

# Apply new migrations
echo "Migrate Successfully Completed"
#python manage.py migrate biodata

python manage.py migrate
#python manage.py createsuperuser --noinput
# Show Migration
#python manage.py showmigrations

#python manage.py migrate biodata --fake
