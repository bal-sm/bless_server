"""quran_server URL Configuration

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
from django.shortcuts import redirect
from django.urls import include
from django.urls import path

from dquran.urls import router as dquran_router
from duser.urls import router as duser_router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda req: redirect("/home/")),
    path("home/", include("duser.urls")),
    path("quran/", include("dquran.urls")),
    path("", include(duser_router.urls)),
    path("", include(dquran_router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
