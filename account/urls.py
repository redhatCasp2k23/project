from django.urls import path
from .views import *

urlpatterns=[
    path('login/',signin,name='account_signin'),
    path('register/',register,name='account_register'),
    path('logout/',logout_action,name='account_logout'),
    path('profile/edit/<int:id>',update,name='update'),
    path('profile/delete/<int:id>',delete,name='delete')
]