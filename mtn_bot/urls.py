from django.urls import path
from . import views

urlpatterns = [
    path('mtn_bot/',views.show, name='show')
]