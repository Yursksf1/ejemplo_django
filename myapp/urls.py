from django.urls import path
from django.views.generic import TemplateView
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    path('florida', TemplateView.as_view(template_name='florida.html'), name='florida'),
    path('cacique', TemplateView.as_view(template_name='cacique.html'), name='cacique'),
    path('', views.lista_centros_comerciales, name='lista_centros_comerciales'),
    path('tiendas', views.lista_centros_tiendas, name='lista_centros_tiendas'),
    path('cc/<str:name_cc>', views.vista_centros_comercial, name='vista_centros_comercial' ),
]
