from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('form', views.feasibility_form_view, name='form'),
    path('service', views.service, name='service'),
    path('form/generate-pdf/', views.generate_pdf, name='generate_pdf'),
]
