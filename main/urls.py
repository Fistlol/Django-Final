from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from main.views.views_set import *
from main.views.views_cbv import *

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('users/', UserViewSet.as_view({'get': 'list'})),
    path('books/', BookAPIView.as_view()),
    path('journals/', JournalAPIView.as_view()),
]