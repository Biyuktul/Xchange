from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

# Create your API's here.

@api_view(['GET'])
def hi_api(request):
    if request.method == 'GET':
        current_time = datetime.now().isoformat()
        response_data = {
            "message": "Hi",
            "timestamp": current_time,
        }
        return Response(response_data, status=status.HTTP_200_OK)