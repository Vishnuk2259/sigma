from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name = 'admin_login'),
    path('',views.admin_home, name = 'admin_home'),
    path('logout/', views.admin_logout, name = 'admin_logout'),
    path('admin/change_password/', views.change_password, name='change_password'),

 
    path('view-banner/',views.banner_view, name = 'banner_view'),
    path('delete-banner/<int:id>', views.delete_banner, name = 'banner_delete'),
    path('edit-banner/<int:id>', views.edit_banner, name = 'banner_edit'),
    path('add-banner/', views.add_banner, name = 'banner_add'),


    path('view-client/',views.client_view, name = 'client_view'),
    path('delete-client/<int:id>', views.delete_client, name = 'client_delete'),
    path('edit-client/<int:id>', views.edit_client, name = 'client_edit'),
    path('add-client/', views.add_client, name = 'client_add'),


    path('view-facility/',views.facilities_view, name = 'facility_view'),
    path('delete-facility/<int:id>', views.delete_facilities, name = 'facility_delete'),
    path('edit-facility/<int:id>', views.edit_facilities, name = 'facility_edit'),
    path('add-facility/', views.add_facilities, name = 'facility_add'),


    path('view-partner/',views.partners_view, name = 'partner_view'),
    path('delete-partner/<int:id>', views.delete_partners, name = 'partner_delete'),
    path('edit-partner/<int:id>', views.edit_partners, name = 'partner_edit'),
    path('add-partner/', views.add_partners, name = 'partner_add'),


    path('view-service/',views.services_view, name = 'service_view'),
    path('delete-service/<int:id>', views.delete_services, name = 'service_delete'),
    path('edit-service/<int:id>', views.edit_services, name = 'service_edit'),
    path('add-service/', views.add_services, name = 'service_add'),

    path('view-gallery/',views.gallery_view, name = 'gallery_view'),
    path('delete-gallery/<int:id>', views.delete_gallery, name = 'gallery_delete'),
    path('edit-gallery/<int:id>', views.edit_gallery, name = 'gallery_edit'),
    path('add-gallery/', views.add_gallery, name = 'gallery_add'),

    path('view-contact/',views.contact_view, name = 'contact_view'),
    path('delete-contact/<int:id>', views.delete_contact, name = 'contact_delete'),
    path('edit-contact/<int:id>', views.edit_contact, name = 'contact_edit'),
    path('add-contact/', views.add_contact, name = 'contact_add'),

    path('view-settings/',views.settings_view, name = 'settings_view'),
    path('delete-settings/<int:id>', views.delete_settings, name = 'settings_delete'),
    path('edit-settings/<int:id>', views.edit_settings, name = 'settings_edit'),
    path('add-settings/', views.add_settings, name = 'settings_add'),

    path('view-team/',views.team_view, name = 'team_view'),
    path('delete-team/<int:id>', views.delete_team, name = 'team_delete'),
    path('edit-team/<int:id>', views.edit_team, name = 'team_edit'),
    path('add-team/', views.add_team, name = 'team_add'),
]