from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('register/',register,name='register'),
    path('service/',service,name='service'),
    path('signIn/',signIN,name='signIn'),
    path('submit/',submit,name='submit'),
    path('login1/',login1,name='login1'),
    path('logout/',logout,name='logout'),
    path('query/',query,name='query'),
    path('show/<str:pk>',show,name='show'),
    path('delete/<int:pk>',delete,name='delete'),
    path('edit/<int:pk>',edit,name='edit'),
    path('update/<int:pk>',update,name='update')
]
