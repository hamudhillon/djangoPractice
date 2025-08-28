from django.shortcuts import render, HttpResponse,redirect
from .models import *
# Create your views here.
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView



def onlineUsers():
    five_min=timezone.now() - timedelta(minutes=5)
    return Profile.objects.filter(last_activity__gte=five_min)

def home(requests):
    # print('a',user.profile.user)
    print(onlineUsers())
    data = {
        'onlineUsers':onlineUsers(),
        'users': [
            {
                'name': 'Ram',
                'phone': 23456789909,
                'status': True,
                'skills': ['html', 'css', 'python']
            },
            {
                'name': 'Sham',
                'phone': 23456789909,
                'status': True,
                'skills': ['html', 'css', 'python']
            },
            
        ]
    }
    # return HttpResponse('Home page from App folder')
    return render(requests, 'home.html', context=data)
# to add html file
# Create templates folder in app folder
# create html file in templates folder
# then in views.py use render to return html file


def about(requests):

    return HttpResponse('About page')



def add(request,num1,num2,name):
    result=num1+num2

    return HttpResponse(f"{result} - {name}")

def data(request):
    data=[
        {'name':'rahul',
        'bio':'a python developer also having knowledge about frontend  '
        },
        {'name':'sham',
        'bio':'a fullstack developer doing present job in isekai.tech'
        },
        {'name':'rohit',
        'bio':'a fullstack developer doing present job in isekai.tech'
        }   
    ]
    return render(request,'index.html',context={'data':data})

def bio(request,name):
    data=[
        {'name':'rahul',
        'bio':'a python developer also having knowledge about frontend'
        },
        {'name':'sham',
        'bio':'a fullstack developer doing present job in isekai.tech'
        } ,
        {'name':'rohit',
        'bio':'a fullstack developer doing present job in isekai.tech'
        }   
    ]
    res=''
    for user in data:
        if user['name'] == name:
            res=user
            break
        else:
            res={'name':'unknown',
                'bio':''
                }
    return render(request,'bio.html',{'bio':res})


def createUsers(request):
    data=[
        {'name':'rahul',
        'bio':'a python developer also having knowledge about frontend'
        },
        {'name':'sham',
        'bio':'a fullstack developer doing present job in isekai.tech'
        } ,
        {'name':'rohit',
        'bio':'a fullstack developer doing present job in isekai.tech'
        }   
    ]
    if request.method=='POST':
        name=request.POST['Name']
        bio=request.POST['bio']
        data.append({'name':name,'bio':bio})
    return render(request,'createUsers.html',{'data':data})


class empViews(ListView):
    model=emp
    template_name='empData.html'
    context_object_name='data'


class empDetailViews(DeleteView):
    model=emp
    template_name='empDetail.html'
    context_object_name='data'


class empCreateView(CreateView):
    model=emp
    template_name='empCreate.html'
    fields=['name','phone','address','department']
    # context_object_name='departments'
    success_url=reverse_lazy('empData')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['departments']=department.objects.all()
        return context

# def empViews(request):
#     data= emp.objects.all()
#     print(data)
#     return render(request,'empData.html',context={'data':data})

def empDelete(request,id):
    empuser=emp.objects.get(id=id)
    print(empuser.name)
    empuser.delete()
    return redirect('empData')

def empUpdate(request,id):
    empUser=emp.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        department=request.POST['department']
        address=request.POST['address']

        # to update values
        empUser.name=name
        empUser.phone=phone
        empUser.department=department
        empUser.address=address
        empUser.save()
        return redirect('empData')
    return render(request,'empEdit.html',context={'data':empUser})

def empCreate(request):
    departments=department.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        departmentValue=request.POST['department']
        address=request.POST['address']

        deptOB=department.objects.get(name=departmentValue)
        emp.objects.create(
            name=name,
            department=deptOB,
            address=address,
            phone=phone
        )
        return redirect('empData')
        # empOB=emp()
        # empOB.name=name
        # empOB.phone=phone
        # empOB.department=department
        # empOB.address=address
        # empOB.save()

    return render(request,'empCreate.html',context={'departments':departments})



def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            print(name,email,message)
    forms=ContactForm()
    return render(request,'contact.html',{'forms':forms})


def studentView(request):
    form=studentForm()
    if request.method=='POST':
        form=studentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request,'students.html',{'forms':form})