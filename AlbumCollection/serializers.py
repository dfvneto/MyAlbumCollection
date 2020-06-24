from rest_framework import serializers
from AlbumCollection.models import Album, Track


# Track Class Serializer
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id','name', 'length', 'music_genre', 'album']


# Album Class Serializer
# Using nested relationship  to represent foreign key
class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['id','name', 'created', 'artist', 'tracks']
