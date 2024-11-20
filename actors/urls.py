from django.urls import path
from . import views

urlpatterns = [
    path('', views.actor_list, name='actor-list'),
    path('<int:actor_id>/', views.actor_detail, name='actor-detail'),
    path('<int:actor_id>/toggle-criminal/', views.toggle_criminal_status, name='toggle-criminal'),
]

