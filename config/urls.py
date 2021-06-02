from django.contrib import admin
from django.urls import path, include
from pybo import views
from pybo.views import base_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    #path('', views.index, name='index'),  # '/' 에 해당되는 path
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]
