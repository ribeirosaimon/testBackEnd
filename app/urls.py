from django.urls import path

from . import views

urlpatterns = [
    path('', views.PlaceListView.as_view(), name="PlaceForm"),
    path('delete/<int:pk>', views.PlaceViewDelete.as_view(), name="delete_place"),
    path('update/<int:pk>', views.PlaceViewupdate.as_view(), name="update_place"),
]