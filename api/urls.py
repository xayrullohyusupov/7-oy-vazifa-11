from . import views
from django.urls import path

urlpatterns = [
    # Contacts
    path('contact_list/', views.contact_list),
    path('contact/detail/<int:id>/', views.contact_detail),
    path('contact/create/', views.contact_create),
    path('contact/update/<int:id>/', views.contact_update, name='contact_update'),
    path('contact/delete/<int:id>/', views.contact_delete, name='contact_delete'),
    # ChooseItems
    path('chooseitems_list/', views.chooseitem_list, name='chooseitem_list'),
    path('chooseitems/detail/<int:id>/', views.chooseitem_detail, name='chooseitem_detail'),
    path('chooseitems/create/', views.chooseitem_create, name='chooseitem_create'),
    path('chooseitems/update/<int:id>/', views.chooseitem_update, name='chooseitem_update'),
    path('chooseitems/delete/<int:id>/', views.chooseitem_delete, name='chooseitem_delete'),
    # Team members
    path('teammembers_list/', views.teammember_list, name='teammember_list'),
    path('teammembers/detail/<int:id>/', views.teammember_detail, name='teammember_detail'),
    path('teammembers/create/', views.teammember_create, name='teammember_create'),
    path('teammembers/update/<int:id>/', views.teammember_update, name='teammember_update'),
    path('teammembers/delete/<int:id>/', views.teammember_delete, name='teammember_delete'),
    # Partners
    path('partners_list/', views.partner_list, name='partner_list'),
    path('partners/detail/<int:id>/', views.partner_detail, name='partner_detail'),
    path('partners/create/', views.partner_create, name='partner_create'),
    path('partners/update/<int:id>/', views.partner_update, name='partner_update'),
    path('partners/delete/<int:id>/', views.partner_delete, name='partner_delete'),
    # Roadmapitems
    path('roadmapitems_list/', views.roadmapitem_list, name='roadmapitem_list'),
    path('roadmapitems/detail/<int:id>/', views.roadmapitem_detail, name='roadmapitem_detail'),
    path('roadmapitems/create/', views.roadmapitem_create, name='roadmapitem_create'),
    path('roadmapitems/update/<int:id>/', views.roadmapitem_update, name='roadmapitem_update'),
    path('roadmapitems/delete/<int:id>/', views.roadmapitem_delete, name='roadmapitem_delete'),
]