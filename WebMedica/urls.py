from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from WebMedica import views



urlpatterns = [

    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('acercade/', views.acercade, name="acercade"),
    path('pacientes/', views.lista_pacientes, name="lista_pacientes"),
    path('pacientes/ficha/', views.ficha, name="ficha"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)