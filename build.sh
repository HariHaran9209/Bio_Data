#!/usr/bin/env bash

source /path/to/your/venv/bin/activate

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
echo "Migrations Successfully Completed"
