from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('addpackage/',views.addPackage,name='addPackage'),
    path('deletepackage/<int:id>/',views.deletePackage,name='deletepackage'),
    path('search/',views.search,name='search')
]