from django.urls import path
from customize import views

urlpatterns = [
    path("", views.index, name="home")
]