from django.contrib.auth.models import User
from django.db import IntegrityError

try:
    superuser = User.objects.create_superuser(
        username="admin",
        email="admin@admin.com",
        password="admin",
    )
    superuser.save()
except IntegrityError:
    print(
        f"Super User with username admin is already present"
    )
except Exception as e:
    print(e)