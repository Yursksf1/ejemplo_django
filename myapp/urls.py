from django.urls import path
from django.views.generic import TemplateView
from myapp import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('florida', TemplateView.as_view(template_name='florida.html'), name='florida'),
    path('cacique', TemplateView.as_view(template_name='cacique.html'), name='cacique'),
    path('centros_comerciales', views.lista_centros_comerciales, name='lista_centros_comerciales'),
]
