from django.urls import path
from task.views import home,secondpage,snippet_detail

urlpatterns = [
    path('', home, name='home'),
    path('snippets/<str:name>', snippet_detail),
    path('secondpage', secondpage, name='secondpage'),
   
]