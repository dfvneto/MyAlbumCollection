from django.urls import path
from AlbumCollection import views
urlpatterns = [
    path('albuns/', views.AlbumList.as_view()),
    path('album/<int:pk>/', views.AlbumDetail.as_view()),
    path('tracks/', views.TrackList.as_view()),
    path('tracks/<int:pk>/', views.TrackDetail.as_view())
]