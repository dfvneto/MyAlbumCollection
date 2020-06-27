from django.urls import include, path
from AlbumCollection.models import Album, Track
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient, URLPatternsTestCase, APIRequestFactory
from rest_framework.test import APIClient


class AlbumTestCase(APITestCase):
    client = APIClient()
    def test_post_album(self):
        # client = APIClient()
        data ={
            "name": "test-album",
            "created": "2020-02-02",
            "artist": "test-artist",
            "tracks": []
        }
        response = self.client.post('/albuns/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Album.objects.count(), 1)
        self.assertEqual(Album.objects.get().name, 'test-album')

    def test_get_album(self):
        response = self.client.get('/albuns/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TrackTestCase(APITestCase):

    def test_get_track(self):
        response = self.client.get('/tracks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    # def test_post_track(self):
    #     # url = ("http://0.0.0.0:8000/tracks/")
    #     url = ('http://127.0.0.1:8000/tracks/')
    #     data ={
    #         "name": "test-track",
    #         "length": "00:00:50",
    #         "music_genre": "test",
    #         "album": 1
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Track.objects.count(), 1) 
    #     self.assertEqual(Track.objects.get().name, 'test-track')