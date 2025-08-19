from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import login ,authenticate,logout

# Create your views here.
def blogAll(request):
    allcats=category.objects.all()
    filters=request.GET
    categoryfilters=''
    if filters:
        categoryfilters=filters['category'].replace('and','&')
    print(categoryfilters)

    allBlogs=blog.objects.filter(category__name__icontains=categoryfilters)
    return render(request,'blogAll.html',context={'blogs':allBlogs,'allcats':allcats})

def blogSingle(request,id,bname):
    singleBlog=blog.objects.get(id=id)
    return render(request,'singleBlog.html',{'blog':singleBlog})

def addPost(request):
    print('aaaaasasdasddas')
    tags=tag.objects.all()
    categories=category.objects.all()
    context={
        'tags':tags,
        'categories':categories
    }
    if request.method=='POST':
        title=request.POST['title']
        ftags=request.POST['tags']
        desc=request.POST['desc']
        cat=request.POST['cat']
        image=request.FILES['image']
        catOB=category.objects.get(id=cat)

        authorOB=author.objects.get(user=request.user)

        allTags=[]
        if ',' in ftags: 
            for t in ftags.split(','):
                mytags=tag.objects.get_or_create(name=t.lower())
                print(mytags)
                if mytags:
                    allTags.append(mytags[0].id)
        postOB=blog.objects.create(
        title=title,
        desc=desc,
        category=catOB,
        image=image,
        created_at=datetime.now(),
        author=authorOB
        )
        postOB.tags.set(allTags)
        postOB.save()

            
        
    return render(request,'addBlog.html',context)


def signup(request):
    if request.method=='POST':
        if request.POST['btn']=='Register':
            username=request.POST['Username']
            email=request.POST['Email']
            password=request.POST['Password']
            name=request.POST['Name']
            userOB=User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=name
            )
            author.objects.create(
                user=userOB
            )
        if request.POST['btn']=='Login':
            username=request.POST['Username']
            password=request.POST['Password']
            userMatch=authenticate(request=request,username= username,password=password)
            if(userMatch):
                login(request=request,user=userMatch)
                return redirect('blogAll')

    return render(request,'signup.html')

def userlogout(request):
    logout(request)
    return redirect('blogAll')

def profileUpdate(request):

    if request.method=='POST':
        Fname=request.POST['Fname']
        Lname=request.POST['Lname']
        Phone=request.POST['phone']
        Email=request.POST['Email']
        FbLink=request.POST['FbLink']
        iglink=request.POST['iglink']
        ProfilePic=request.FILES['profilePic']
        
        userOB=User.objects.get(id=request.user.id)
        userOB.first_name=Fname
        userOB.last_name=Lname
        userOB.email=Email

        userOB.save()


        authorOb=author.objects.get(user=request.user)
        authorOb.phone=Phone
        authorOb.Fb_link=FbLink
        authorOb.ig_link=iglink
        authorOb.profilePic=ProfilePic

        authorOb.save()    

    myauthor=author.objects.get(user=request.user)

    return render(request,'profileUpdate.html',{'myauthor':myauthor})