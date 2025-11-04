from django.urls import path
from .views import hello, goodbye, edad, primer_plantilla, segunda_plantilla , tercera_plantilla  

urlpatterns = [
   path('hello/', hello, name='hello'),  # Placeholder for aulas app URLs
   path('goodbye/', goodbye, name='goodbye'),  # New URL pattern for goodbye view
   path('edad/<int:anios>/<int:futuro>', edad, name='edad'),  # New URL pattern for edad view
   path('plantilla', primer_plantilla, name='primer_plantilla'),  # New URL pattern for primer_plantilla view
   path('segunda_plantilla', segunda_plantilla, name='segunda_plantilla'),  # New URL pattern for segunda_plantilla view
   path('tercera_plantilla', tercera_plantilla, name='tercera_plantilla'),  # New URL pattern for tercera_plantilla view
   ]
