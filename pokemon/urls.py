from django.urls import path
from pokemon.views import url_input

urlpatterns = [
    path('', url_input),
]
