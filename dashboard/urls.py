from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contactList', views.contactList, name='contactList'),
    path('contact/update/<int:id>/', views.updateStatus, name='updateStatus'),
]
