from django.urls import path
from .views import hello, goodbye, edad, primera_plantilla, segunda_plantilla , tercera_plantilla , cuarta_plantilla, crear_musico, crear_album 

urlpatterns = [
   path('hello/', hello, name='hello'),  # Placeholder for aulas app URLs
   path('goodbye/', goodbye, name='goodbye'),  # New URL pattern for goodbye view
   path('edad/<int:anios>/<int:futuro>', edad, name='edad'),  # New URL pattern for edad view 
   path('primera_plantilla', primera_plantilla, name='primera_plantilla'),  # New URL pattern for primer_plantilla view
   path('segunda_plantilla', segunda_plantilla, name='segunda_plantilla'),  # New URL pattern for segunda_plantilla view
   path('tercera_plantilla', tercera_plantilla, name='tercera_plantilla'),  # New URL pattern for tercera_plantilla view
   path('cuarta_plantilla', cuarta_plantilla, name='cuarta_plantilla'),  # New URL pattern for cuarta_plantilla view
   path('crear_musico/<str:nombre>/<str:apellido>/<str:instrumento>/', crear_musico, name='crear_musico'),  # New URL pattern for crear_musico view
   path ('crear_album/<str:nombre>/<int:estrellas>/<int:artista_id>/', crear_album, name='crear_album'),  # New URL pattern for crear_album view    
   ]










   