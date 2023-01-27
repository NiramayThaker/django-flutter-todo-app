from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
			'description': 'Creates new note with data sent in post req'
		},
		{
			'Endpoint': '/notes/id/update/',
			 'method': 'PUT',
			 'body': {'body': ""},
			 'description': 'Creates an existing note with data sent it back'
		 },
		{
			'Endpoint': '/ notes / id / delete / ',
			'method': 'DELETE',
			' body': None,
			'description': 'Deletes and exiting note'
		},
	]

	return JsonResponse(routes, safe=False)
