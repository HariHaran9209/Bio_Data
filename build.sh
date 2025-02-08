#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Show existing migrations
echo "Showing Migrations"
python manage.py showmigrations

# Run migrations to ensure the latest migration files are applied first
echo "Running Migrations"
python manage.py migrate

# Flushing the database (this is only useful if you need to reset data in your tables)
echo "Flushing The Database"
python manage.py flush --noinput

# Check the SQL that would be executed by flush
echo "Executing SQL Flush"
python manage.py sqlflush

# Generate migrations if any new model changes exist
echo "Migrations starts"
python manage.py makemigrations biodata

# Apply new migrations
echo "Migrations Successfully Completed"
python manage.py migrate biodata
echo "Migrate Successfully Completed"
