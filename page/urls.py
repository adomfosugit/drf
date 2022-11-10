from django.urls import path
from django.views.generic import TemplateView
# Template View too render basic 
# page which generally outputs data from database

app_name = 'page'

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'page/index.html'))
    
    
]