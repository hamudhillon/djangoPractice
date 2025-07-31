from django.shortcuts import render, HttpResponse

# Create your views here.


def home(requests):
    data = {
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