# testBackEnd

Bom dia, 

# Execute nessa ordem
sudo docker-compose up -d --build
sudo docker-compose exec web python manage.py makemigrations app --noinput
sudo docker-compose exec web python manage.py migrate --noinput

# Aqui você deve criar o admin que fará login
sudo docker-compose exec web python manage.py createsuperuser

* Não consegui adicionar postgres no Docker, tenho conhecimento básico de docker
* Não consegui adicionar a funcionalidade localizar por (area geo, bbox) 
