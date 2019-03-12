from django.contrib import admin
from django.urls import path, include
from apstatus import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apstatus/', views.index, name='index'),
    path('', views.index, name='index')
    #path('apstatus/', include('apstatus.urls')), #apstatus.urls.py index is not defined
    #path('', include('apstatus.urls')) #apstatus.urls.py index is not defined

]