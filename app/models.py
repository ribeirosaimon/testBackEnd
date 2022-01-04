from django.db import models
from django.contrib.auth import get_user_model

class Place(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=100)
    lat = models.CharField("Latitude", max_length=100)
    log = models.CharField("Longetude", max_length=100)
    visit = models.BooleanField()
    timestamp = models.DateField("Date")

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"

    def __str__(self) -> str:
        return self.name