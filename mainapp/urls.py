from django.urls import path
from . import views


urlpatterns=[
path('',views.home,name="home"),
path('submitPage', views.submitPage, name="submitPage"),
path('x',views.submitPage,name="x")


#path("<str:username>",views.post, name="post")

]