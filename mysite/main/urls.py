from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('view', views.view),
    path('view/<int:id>', views.view_zapis),
    path('create', views.create),
]