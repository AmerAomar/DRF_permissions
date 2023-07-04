from .models import Thing, Post
from rest_framework import serializers

class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing # this is the model that we are serializing
        fields = ('id','Thing_name', 'user_name', 'description', 'created_at', 'updated_at') # these are the fields that we want to be able to access from the model


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post # this is the model that we are serializing
        fields = ('id','title', 'desc', 'created_at', 'updated_at') # these are the fields that we want to be able to access from the model