#!/bin/bash
# Install Python dependencies
pip install -r requirements.txt

# Run Django collectstatic command to gather static files
python manage.py collectstatic --noinput
