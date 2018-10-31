# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def about(request):
    return render(request, 'personal/about.html')

def overview(request):
    return render(request, 'personal/overview.html')
