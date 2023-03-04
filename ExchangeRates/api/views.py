import os
import json

from django.conf import settings
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView


path = os.path.join(f'{settings.BASE_DIR}/..', 'Parser', 'data.json')


class GetAllAPIView(APIView):
    def get(self, request):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
        
        return Response(data)


class GetAPIView(APIView):
    def get(self, request, name):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
        
        for item in data:
            if item['name'] == name:
                return Response(item)
        
        return Response({'detail': 'Не знайденно.'}, status=HTTP_404_NOT_FOUND)
