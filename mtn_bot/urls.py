from django import path
from . import views

urlpatterns = [
    path('show/',views.show, name='show')
]