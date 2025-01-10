from django.urls import path
from .views import *                                                                                                                            

urlpatterns = [
    path('spells/', SpellAPIView.as_view(), name='spell' )
]