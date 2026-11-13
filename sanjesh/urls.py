from django.urls import path
from .views import sanjesh

app_name = 'sanjesh'

urlpatterns = [
    path('', sanjesh, name='sanjesh'),
]
