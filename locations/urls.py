from django.urls import path
from locations import views
urlpatterns = [
    path('', views.index, name="locations.index"),
    path('<int:location_id>', views.show, name="locations.show"),
    path('all', views.get_all_locations, name="locations.all")
]
