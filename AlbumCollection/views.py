from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from AlbumCollection.models import Album, Track
from AlbumCollection.serializers import AlbumSerializer,TrackSerializer
# Create your views here.


class AlbumList(APIView):
    def get(self,request,fomart=None):
        albums = Album.objects.all()
        serialized_album = AlbumSerializer(albums, many=True)
        return Response(serialized_album.data)

    def post(self,request, fomart = None):
        data = JSONParser().parse(request)
        serialized_album = AlbumSerializer(data=data)
        if serialized_album.is_valid():
            serialized_album.save()
            return Response(serialized_album.data, status=status.HTTP_201_CREATED)
        return Response(serialized_album.errors,status=status.HTTP_400_BAD_REQUEST)


class AlbumDetail(APIView):
    def get_object(self,pk):
        try:
            album = Album.objects.get(pk=pk)
            return album
        except Album.objects.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        album = self.get_object(pk)
        serialized_album = AlbumSerializer(album)
        return Response(serialized_album.data)


class TrackList(APIView):
    def get(self,request,fomart=None):
        tracks = Track.objects.all()
        serialized_tracks = TrackSerializer(tracks, many=True)
        return Response(serialized_tracks.data)
    
    def post(self,request,fomart=None):
        data = JSONParser().parse(request)
        serialized_track = TrackSerializer(data=data)
        if serialized_track.is_valid():
            serialized_track.save()
            return Response(serialized_track.data,status=201)
        return Response(serialized_track.errors,status=status.HTTP_400_BAD_REQUEST)


class TrackDetail(APIView):
    def get_object(self,pk):
        try:
            track = Track.objects.get(pk=pk)
            return track
        except Track.objects.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        track = self.get_object(pk)
        serialized_track = TrackSerializer(track)
        return Response(serialized_track.data)
