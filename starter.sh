#!/bin/bash
echo "Apply database migrations"
python3 manage.py migrate --noinput
python3 manage.py makemigrations --noinput
echo "runing script"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell
#python manage.py shell < "utils/create_superuser.py"
# Start server
echo "Starting server"
python3 manage.py runserver 0.0.0.0:8000