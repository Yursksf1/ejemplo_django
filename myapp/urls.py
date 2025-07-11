from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('florida', TemplateView.as_view(template_name='florida.html'), name='florida'),
    path('cacique', TemplateView.as_view(template_name='cacique.html'), name='cacique'),
]
