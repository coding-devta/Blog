from django.shortcuts import render
from .form import *
import random
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.



def logout_view(request):
    logout(request)

    return redirect('/login/')

def home(request):
    context = {
        'blogs' : blogmodel.objects.all(),
        'blog_first' : blogmodel.objects.all()[:1].get()
    }

    return render(request ,'home.html',context)

def login_view(request):
    return render(request ,'login.html')

def register_view(request):

    return render (request,'register.html')

def add_blog_view(request):
    context = {

        'form' : blogform,
    }
    try:
      if request.method == 'POST':
            form = blogform(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user= request.user

            if form.is_valid():
               description = form.cleaned_data['description']
              
            
            blog_obj = blogmodel.objects.create(
                title=title , image=image,user=user,description= description,
            )

            return redirect ('/addblog/')
    
    
    except Exception as e:
        print(e)

    
    return render (request,'add_blog.html', context)

    # def see_blog_view(request):
    #     return render(request,'see_blog.html')
    
    
def blog_detail_view(request,slug):
        context ={}
        try:
            blog_obj = blogmodel.objects.filter(slug=slug).first()
           
            context['blog_obj'] = blog_obj
        except Exception as e:
            print(e)

        return render(request,'blog_detail.html',context)
    
def see_blog_view(request):
    context = {}
    try:
        blog_objects = blogmodel.objects.filter(user=request.user)
           
        context['blog_objects'] = blog_objects
    
    except Exception  as e:
        print(e)
    return render(request,'seeblog.html',context)

def delete_view(request, slug):
    # try:
    #     delete_obeject = blogmodel.objects.get(id=id)
    #     if delete_obeject.user == request.user:
    #         delete_object.delete()
    # except Exception as e:
    #     print(e)
    try:
        blog_obj = blogmodel.objects.get(slug = slug)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)
    
    return redirect('/seeblog/')



def blog_update(request , slug):
    context = {}
    try:
        
        
        blog_obj = blogmodel.objects.get(slug = slug)
       
        
        if blog_obj.user != request.user:
            return redirect('/')
        
        initial_dict = {'description': blog_obj.description}
        form = blogform(request.POST or None , initial = initial_dict)
        # if request.method == 'POST':
        #     form = blogform(request.POST)
            
        #     image = request.FILES['image']
        #     title = request.POST.get('title')
        #     user = request.user
            
        #     if form.is_valid():
        #         description = form.cleaned_data['desciption']
            
        #     blog_obj = blogmodel.objects.create(
        #         user = user , title = title, 
        #         description = description , image = image
        #     )
        if request.method == 'POST':
            form = blogform(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user= request.user

            if form.is_valid():
               description = form.cleaned_data['description']
              
            
            blog_obj = blogmodel.objects.create(
                title=title , image=image,user=user,description= description,
            )

        
        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e :
        print(e)

    return render(request , 'update.html' , context)


def verify (request , token):
    try:
        profile_obj = profile.objects.filter(token = token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
            return redirect('/login/')
    except Exception  as e:
        print(e)


    return redirect('/') 