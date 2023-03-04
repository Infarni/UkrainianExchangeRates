from django.urls import path
from api.views import GetAllAPIView, GetAPIView


urlpatterns = [
    path('', GetAllAPIView.as_view()),
    path('<str:name>/', GetAPIView.as_view())
]
