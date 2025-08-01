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