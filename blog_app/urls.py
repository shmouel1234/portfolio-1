from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    
    path('<int:id>/', views.detail, name='details'),
]
