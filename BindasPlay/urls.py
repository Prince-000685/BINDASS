"""BindasPlay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import userview
from .import auto
from .import kalyanViews
from . import adminviews

urlpatterns = [
    
    path('',userview.Userview),

    path('displayresult/',userview.displayResult),
    path('saveresult/',userview.saveResult),
    path('searchAll/',userview.SearchAll),
    path('search/',userview.SearchByDate),
    path('',include('authentication.urls')),
    path('notification/',userview.Notification),
    path('addNotification/',userview.AddNotification),
    path('typeSubmit1/',auto.TypeSubmit1),
    path('typeSubmit2/',auto.TypeSubmit2),
    path('typeSubmit3/',auto.TypeSubmit3),

    path('displayresultkalyan/',kalyanViews.displayResultKalyan),
    path('saveresultkalyan/',kalyanViews.saveResultKalyan),
    path('searchAllkalyan/',kalyanViews.SearchAllKalyan),
    path('searchkalyan/',kalyanViews.SearchByDateKalyan),
    path('typeSubmitkalyan1/',auto.TypeSubmitKalyan1),
    path('typeSubmitkalyan2/',auto.TypeSubmitKalyan2),
    path('typeSubmitkalyan3/',auto.TypeSubmitKalyan3),    

    #adminworks

    path('atypeSubmit1/',adminviews.ATypeSubmit1),
    path('atypeSubmit2/',adminviews.ATypeSubmit2),
    path('atypeSubmit3/',adminviews.ATypeSubmit3),
    path('atypeSubmitkalyan1/',adminviews.ATypeSubmitKalyan1),
    path('atypeSubmitkalyan2/',adminviews.ATypeSubmitKalyan2),
    path('atypeSubmitkalyan3/',adminviews.ATypeSubmitKalyan3),
    path('asaveresult/',adminviews.AsaveResult),
    path('asaveresultkalyan/',adminviews.AsaveResultKalyan),
]
