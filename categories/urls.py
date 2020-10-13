from django.urls import path
from categories import views

urlpatterns = [
    path('', views.index, name="categories.index"),
    path('<int:category_id>', views.show, name="categories.show"),
    path('all/', views.all_categories, name="categories.all"),
]
