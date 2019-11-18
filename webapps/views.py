# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import WordpressForm

import os

# Create your views here.

def index(request):
    return render(request, 'base.html')

def newProject(request):
    
    return render(request, 'project.html')

def wordpress(request):
    a = WordpressForm()
    return render(request, 'wordpress.html', {'f': a})

def ghost(request):
    return render(request, 'ghost.html')