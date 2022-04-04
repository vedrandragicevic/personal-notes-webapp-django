from notes.models import Note
from users.models import Profile
from .serializers import NoteSerializer, ProfileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@api_view(['GET'])
def getRoutes(request):
    """
        Shows all available routes in the app.
    """
    routes = [
        {
            'GET': '/api/notes/'
            },
        {
            'GET': '/api/notes/id'
            },
        {
            'GET': '/api/profiles/'
            },
        {
            'POST': '/api/token'
            },
        {
            'POST': '/api/token/refresh'
            }
    ]

    return Response(routes)


# Permission classes decorator limits user to see projects only if he's authenticated
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    notes = Note.objects.all()
    # Takes query set and transforms it into JSON
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    # Takes query set and transforms it into JSON
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfiles(request):
    profiles = Profile.objects.all()
    # Takes query set and transforms it into JSON
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)
