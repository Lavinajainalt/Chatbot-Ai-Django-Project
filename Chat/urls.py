from django.urls import path
from . import views

urlpatterns = [
    path('api/chat/', views.gemini_chat_api, name='gemini_chat_api'),
    path('api/models/', views.list_models, name='list_models'),
    path('Chatpanel/', views.Chatpanel, name='Chatpanel'),
]
