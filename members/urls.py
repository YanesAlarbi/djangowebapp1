from django.urls import  path
from . import views

urlpatterns=[
    path('',views.main,name='main'),
    path('members/',views.members,name='members'),
    path('members/details/<int:id>',views.details,name='details'),
    path('testing/',views.testing,name='testing'),
    path('testview/',views.testview,name='testview'),
    path('test2/',views.test2,name='test2')

]