

from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat_home'),  # Add this line
    path('api/chat/', views.chat_api, name='chat_api'),
]