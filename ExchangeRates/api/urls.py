from django.urls import path
from api.views import index, GetAllAPIView, GetAPIView


urlpatterns = [
    path('', index),
    path('<str:currency>/', GetAllAPIView.as_view()),
    path('<str:currency>/<str:name>/', GetAPIView.as_view())
]
