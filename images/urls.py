from django.urls import path
from images import views

urlpatterns = [
    path('search/', views.search, name="images.search")
]
