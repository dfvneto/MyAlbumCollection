from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from AlbumCollection.models import Album, Track
from AlbumCollection.serializers import AlbumSerializer, TrackSerializer
from django.core.exceptions import ObjectDoesNotExist


# Functions to get objects from database using given pk
def get_album_object(pk):
    try:
        album = Album.objects.get(pk=pk)
        return album
    except ObjectDoesNotExist:
        raise Http404


def get_track_object(pk):
    try:
        track = Track.objects.get(pk=pk)
        return track
    except ObjectDoesNotExist:
        raise Http404


# Listing and adding albuns
class AlbumList(APIView):
    def get(self, request, fomart=None):
        albums = Album.objects.all()
        serialized_album = AlbumSerializer(albums, many=True)
        serialized_album_data = serialized_album.data
        for album in serialized_album_data:
            for track in album['tracks']:
                track.pop('album', None)
        return Response(serialized_album.data)

    def post(self, request, fomart=None):
        data = JSONParser().parse(request)
        serialized_album = AlbumSerializer(data=data)
        if serialized_album.is_valid():
            serialized_album.save()
            return Response(serialized_album.data, status=status.HTTP_201_CREATED)
        return Response(serialized_album.errors, status=status.HTTP_400_BAD_REQUEST)


# Getting album detail
class AlbumDetail(APIView):
    def get(self, request, pk, format=None):
        album = get_album_object(pk)
        serialized_album = AlbumSerializer(album)
        return Response(serialized_album.data)


# Listing and adding tracks
# To add a new track it is necessary to create album first.
# The request waits for the id of the track's album
class TrackList(APIView):
    def get(self, request, fomart=None):
        tracks = Track.objects.all()
        serialized_tracks = TrackSerializer(tracks, many=True)
        serialized_tracks_data = serialized_tracks.data
        album_id = 0
        for item in serialized_tracks_data:
            if album_id != item['album']:
                album_id = item['album']
                album = get_album_object(album_id)
            serialized_album = AlbumSerializer(album)
            item['album'] = serialized_album.data['name']
        return Response(serialized_tracks_data)

    def post(self, request, fomart=None):
        serialized_track = TrackSerializer(data=request.data)
        if serialized_track.is_valid():
            serialized_track.save()
            return Response(serialized_track.data, status=201)
        return Response(serialized_track.errors, status=status.HTTP_400_BAD_REQUEST)


# Getting Track Details
class TrackDetail(APIView):
    def get(self, request, pk, format=None):
        track = get_track_object(pk)
        serialized_track = TrackSerializer(track)
        serialized_track_data = serialized_track.data
        album = get_album_object(serialized_track.data['album'])
        serialized_album = AlbumSerializer(album)
        serialized_track_data['album'] = serialized_album.data['name']
        return Response(serialized_track_data)
