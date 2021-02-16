from django.conf.urls import url, include
from django.db import router
from django.urls import path
from addresses import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addresses/', views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('login/', views.login),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]