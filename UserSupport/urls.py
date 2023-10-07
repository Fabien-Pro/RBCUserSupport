from django.urls import path
from .views import (
    user_register_view,index_view,request_dashboard_view

)

urlpatterns = [
    path('',index_view, name='index'),
    path('register/',user_register_view.as_view(), name='register'),
   
    path('requestdashboard/',request_dashboard_view, name='requestdashboard'),
]