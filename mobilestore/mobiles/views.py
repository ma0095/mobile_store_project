from django.shortcuts import render,redirect
from django.views.generic import View
from mobiles.models import Mobile
from mobiles.forms import MobileCreateForm
from django.contrib import messages


class MobileCreateView(View):
    def get(self,request,*args,**kwargs):
        form=MobileCreateForm
        return render(request,"mob-add.html",{"form":form})

class MobileListView(View):
    def









