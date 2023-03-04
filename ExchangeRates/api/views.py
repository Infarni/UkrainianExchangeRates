import os
import json

from django.conf import settings
from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView


currencys = ['usd', 'eur', 'gbp', 'chf']


def index(request):
    return redirect('usd/')


class GetAllAPIView(APIView):
    def get(self, request, currency):
        if not currency in currencys:
            return Response({'detail': 'Не знайдено.'}, status=HTTP_404_NOT_FOUND)
    
        path = os.path.join(f'{settings.BASE_DIR}/..', 'Parser', f'{currency}.json')
        with open(path, 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
        
        return Response(data)


class GetAPIView(APIView):
    def get(self, request, currency, name):
        if not currency in currencys:
            return Response({'detail': 'Не знайдено.'}, status=HTTP_404_NOT_FOUND)

        path = os.path.join(f'{settings.BASE_DIR}/..', 'Parser', f'{currency}.json')
        with open(path, 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
        
        for item in data:
            if item['name'] == name:
                return Response(item)
        
        return Response({'detail': 'Не знайдено.'}, status=HTTP_404_NOT_FOUND)
