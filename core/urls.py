from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('portfolio/<pk>/',portfolioview,name='portfolio'),
    path('contact/',contactform,name='contact')
]