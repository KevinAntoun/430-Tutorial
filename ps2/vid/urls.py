from django.urls import path
from . import views

app_name = 'vid'

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('videos/new/', views.video_create, name='video_create'),
    path('videos/<int:pk>/', views.video_detail, name='video_detail'),
    path('videos/<int:pk>/edit/', views.video_update, name='video_update'),
    path('videos/<int:pk>/delete/', views.video_delete, name='video_delete'),
]
