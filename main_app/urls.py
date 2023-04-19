
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('about/', views.about, name='about'),

  path('snakes/', views.snakes, name='snakes'),

  path('snake/<int:snake_id>/', views.snake_detail, name='snake_detail'),

  path('snake/<int:snake_id>/add_feeding/', views.add_feeding, name='add_feeding'),

  path('snake/<int:snake_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),

  path('snake/<int:snake_id>/remove_toy/<int:toy_id>/', views.remove_toy, name='remove_toy'),

  path('snake/create/', views.SnakeCreate.as_view(), name='snake_create'),

  path('snake/<int:pk>/update/', views.SnakeUpdate.as_view(), name='snake_update'),

  path('snake/<int:pk>/delete/', views.SnakeDelete.as_view(), name='snake_delete'),

  path('toys/', views.toys, name='toys'),

  path('toy/<int:toy_id>/', views.toy_detail, name='toy_detail'),

  path('toy/create/', views.ToyCreate.as_view(), name='toy_create'),

  path('toy/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy_update'),

  path('toy/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy_delete'),
]