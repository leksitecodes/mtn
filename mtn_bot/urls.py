from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_response, name='get_response'),
    path('', views.chat_page, name='home'),  # Add this line to make chat page the home page
]



