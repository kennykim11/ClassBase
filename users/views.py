from django.shortcuts import render
from django.http import HttpResponse
from .models import student
from django.shortcuts import render
from courses.models import *
from django.utils.timezone import now, localtime

# Create your views here.

def myFunc(request):
    '''s = student.objects.get(id=1) #queries students
    print(s.get_username())

    student.objects.create(id=1).save()'''
    return render(request, "base.html", {'user': "kenny", "courses":Section.objects
                  .get(start_time >= localtime(now()).time())
                  .get(end_time <= localtime(now()).time())
                  .get(model)})