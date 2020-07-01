from django.urls import path
from AlbumCollection import views
urlpatterns = [
    path('albuns/', views.AlbumList.as_view()),
    path('album/<int:pk>/', views.AlbumDetail.as_view()),
    path('tracks/', views.TrackList.as_view()),
    path('track/<int:pk>/', views.TrackDetail.as_view()),
    path('chat/', views.index),
    path('chat/<str:room_name>/', views.room, name='room'),
]