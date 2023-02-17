from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
        'Endpoint': '/notes/',
        'method': 'GET',
        'body': None,
        'description': 'Returns an array of notes'
        },
        {
        'Endpoint': '/notes/id',
        'method': 'GET',
        'body': None,
        'description': 'Returns a single note of object'
        },
        {
        'Endpoint': '/notes/create/',
        'method': 'POST',
        'body': {'body': ""},
        'description': 'Creates a new note with data sent in post req'
        },
        {
        'Endpoint': '/notes/update/',
        'method': 'PUT',
        'body': {'body': ""},
        'description': 'Updates an existing note'
        },
        {
        'Endpoint': '/notes/delete/',
        'method': 'DELETE',
        'body': None,
        'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

# Get all notes
@api_view(['GET'])
def getNotes(requset):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

# Get a single note by id
@api_view(['GET'])
def getNote(requset, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

# Create a note
@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

# Update a note
@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data

    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Delete a note
@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')
