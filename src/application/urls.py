from django.urls import path
from .views import index, sect1, sect2, sect3, accueil

urlpatterns = [
    path('', index, name="application-index"),
    path('sect1/', sect1, name='sect1'),
    path('sect2/', sect2, name='sect2'),
    path('sect3/', sect3, name='sect3'),
    path('accueil/', accueil, name='accueil'),
]