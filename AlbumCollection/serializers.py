from rest_framework import serializers
from AlbumCollection.models import Album, Track



class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['name', 'length', 'music_genre', 'album']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['name', 'created', 'artist', 'tracks']
