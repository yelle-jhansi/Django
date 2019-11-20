# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from stock.models import UserProfile
from django.http import HttpResponse
# Create your views here.
def homeview(request):
	return render(request,"stock/home.html")

def user_profile(request):
	data = UserProfile.objects.all()
	print data
	return HttpResponse("result %s"%data)
