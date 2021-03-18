"""portfolio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings

from portfolio_app import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    
    path('', views.home, name='home'),
    
    path('blog/', include('blog_app.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# the static function does not return a single url,
# so you can not add it as a single element to the list.
# By using +=, you actually append all the elements of
# the result of the static call to the list.