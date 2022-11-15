from django.urls import path
from . import views as chat_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('', chat_view.home, name="chat-home"),
    path('checkroom/', chat_view.checkroom, name="check-room"),
    path('send/', chat_view.send, name="send"),
    path('<str:room>/', chat_view.room, name="room"), 
    path('getMessages/<str:room>/', chat_view.getMessages, name='getMessages'),
    # path('getMessages/<int:pk>/', chat_view.getMessages, name='getMessages'),
    
]