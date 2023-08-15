from django.contrib import admin
from django.urls import path
from . import views
from . import admin

urlpatterns = [
     path('userlogin',views.userLogin),
     path('adminlogin/',admin.adminLogin),
     path('updatePassword/',admin.updatePassword),
     path('adduserPage/',admin.AddUserPage),
     path('addUser/',admin.AddUser),
     path('updateAdminPasspage/',admin.updateAdminPasspage),
     path('updateAdminPass/',admin.updateAdminPass),

]