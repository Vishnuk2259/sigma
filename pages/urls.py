from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('clients/', views.client, name = 'client'),
    path('contact/', views.contact, name = 'contact'),
    path('facilities/', views.facilities, name = 'facilities'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('partners/', views.partners, name = 'partners'),
    path('profile/', views.profile, name = 'profile'),
    path('services/', views.services, name = 'services'),
    path('team/', views.team, name = 'team'),
    path('submit_contact_form/', views.submit_contact_form, name='submit_contact_form'),
    # path('send-email/<int:contact_id>/', views.send_email, name='send_email')
]