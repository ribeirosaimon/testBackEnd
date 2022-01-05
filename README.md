# testBackEnd
Back end test

sudo docker-compose up -d --build
sudo docker-compose exec django python manage.py makemigrations --noinput
sudo docker-compose exec django python manage.py migrate --noinput
sudo docker-compose exec django python manage.py createsuperuser