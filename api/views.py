from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


# A user can only get this data using GET request
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
			'description': 'Returns a single note object'
		},
		{
			'Endpoint': '/notes/create/',
			'method': 'POST',
			'description': 'Creates new note with data sent in post reqest'
		},
		{
			'Endpoint': '/notes/id/update/',
			 'method': 'PUT',
			 'body': {'body': ""},
			 'description': 'Creates an existing note with data sent in post request'
		 },
		{
			'Endpoint': '/ notes / id / delete / ',
			'method': 'DELETE',
			' body': None,
			'description': 'Deletes and exiting note'
		},
	]

	return Response(routes)

@api_view(['GET'])
def getNotes(request):
	notes = Note.objects.all()

	# It will serialize multiple obj. from the query (many=True)
	serialized_notes = NoteSerializer(notes, many=True)

	return Response(serialized_notes.data)

@api_view(['GET'])
def getNotesByID(request, pk):
	notes = Note.objects.get(id=pk)
	serialized_note = NoteSerializer(notes, many=False)

	return Response(serialized_note.data)


@api_view(['POST'])
def createNote(request):
	data = request.data
	note = Note.objects.create(
		body=data['body'],
	)
	serialized_note = NoteSerializer(note, many=False)

	return Response(serialized_note.data)

@api_view(['PUT'])
def updateNote(request, pk):
	note = Note.objects.get(id=pk)
	serializer = NoteSerializer(note, data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)
