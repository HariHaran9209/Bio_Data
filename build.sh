#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

python manage.py makemigrations
echo "Migrations Successfully Completed"

# Apply new migrations
echo "Migrate Successfully Completed"
python manage.py migrate

# Show Migration
python manage.py showmigrations
