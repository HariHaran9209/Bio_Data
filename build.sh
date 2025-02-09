#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Migration For Biodata
python manage.py makemigrations biodata
echo "Migrations For biodata"

# Generate migrations if any new model changes exist
echo "Migrations starts"
python manage.py makemigrations
echo "Migrations Successfully Completed"

# Apply new migrations
echo "Migrate Successfully Completed"
python manage.py migrate

# Show Migration
python manage.py showmigrations
