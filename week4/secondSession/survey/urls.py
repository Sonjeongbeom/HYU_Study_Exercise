from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name="main"),
    path('new', new, name='new'),
    path('create', create, name='create'),
    path('save', save, name='survey'),
    path('result/<int:surveyIdx>', result, name='result'),
]