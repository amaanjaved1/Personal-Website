from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import admin
from django.urls import reverse
from pyparsing import opAssoc
from django.core.mail import send_mail, BadHeaderError
from .models import Subscriber
from django import forms
from django.forms import ModelForm, ValidationError


class EmailForm(ModelForm):
    class Meta: 
        model = Subscriber
        fields = ["name", "email"]

def index(request):
    return render(request, "content/index.html")

def projects(request):
    return render(request, "content/projects.html")

def resume(request):
    return render(request, "content/resume.html")

def contact_me(request):
     return render(request, "content/contact.html", {
         "form": EmailForm
     })