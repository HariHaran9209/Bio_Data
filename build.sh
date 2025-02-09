#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Generate migrations if any new model changes exist
echo "Migrations starts"
python manage.py makemigrations biodata
echo "Migrations Successfully Completed"

# Apply new migrations
python manage.py migrate biodata
echo "Migrate Successfully Completed"
python manage.py migrate
