from django.urls import path
from mobiles import views

urlpatterns=[
    path("add",views.MobileCreateView.as_view()),

]