from django.contrib import admin
from django.urls import path,include
from enrollment_app import views

urlpatterns = [
    path('',views.HomeView,name='home_view_link'),
    path('saveData/',views.save_data,name='save_data_link'),
    path('deleteData/',views.del_data,name='delete_data_link'),
    path('eiditData/',views.edit_data,name='edit_data_link')
]
