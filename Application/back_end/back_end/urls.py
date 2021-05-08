"""back_end URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url

from back_end.auth_login import auth_login, get_user_info, return_2_step_code, auth_logout

urlpatterns = [
    url(r'^auth/login', auth_login),
    url(r'^user/info', get_user_info),
    url(r'^auth/2step-code', return_2_step_code),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/logout', auth_logout)
]
