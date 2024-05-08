from django.urls import path
from . import views

urlpatterns = [
    path('cosmetics/', views.cosmetics),
    path('cosmetics/<int:cosmetic_id>/', views.cosmetic),
    path('users/', views.users),
    path('users/<int:user_id>/', views.user),
    path('add_user/', views.add_user),
    path('add_cosmetic/', views.add_cosmetic),
    path('change_rating/<int:cosmetic_id>/<int:user_id>/', views.change_rating),
]
