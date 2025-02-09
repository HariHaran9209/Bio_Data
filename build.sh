#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

python manage.py makemigrations biodata
echo "Migrations Successfully Completed"

# Apply new migrations
echo "Migrate Successfully Completed"
python manage.py migrate biodata

# Show Migration
python manage.py showmigrations
