
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('page.urls', namespace = 'page' )),
        path('api/', include('page_api.urls', namespace= 'page_api')),
    
]
