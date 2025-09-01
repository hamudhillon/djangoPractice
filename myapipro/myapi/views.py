from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import *

import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Create your views here.


def home(request):
    return JsonResponse({'Name':'asdasghj'})

def student_list(request):
    students=list(Student.objects.values())
    return JsonResponse(students,safe=False)

def student_details(request,id):
    student=Student.objects.get(id=id)
    return JsonResponse({
        'id':student.id,
        'name':student.name,
        'email':student.email,
        'age':student.age
    })


@csrf_exempt
@require_http_methods(['POST'])
def student_create(request):
    print(request)