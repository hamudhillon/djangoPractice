from django.shortcuts import render
from .models import *
from datetime import datetime


# Create your views here.
def blogAll(request):
    allBlogs=blog.objects.all()
    return render(request,'blogAll.html',context={'blogs':allBlogs})

def blogSingle(request):

    return render(request,'singleBlog.html')

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
        created_at=datetime.now()
        )
       
        postOB.tags.set(allTags)
        postOB.save()

            
        
    return render(request,'addBlog.html',context)