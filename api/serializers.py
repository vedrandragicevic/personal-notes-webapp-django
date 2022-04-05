from rest_framework import serializers
from notes.models import Note
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    slug_field='profile'
    
    class Meta:
        model = Note
        fields = '__all__'
