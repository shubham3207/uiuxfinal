

# Create your views here.

from .models import *
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django. contrib import messages




# Create your views here.



def homepage(request):
    views = {}
    views['blogs'] = Blog.objects.all()
    
    return render(request,'home.html',views)





def blog_single(request,id):
    views = {}
    views['blog_details'] = Blog.objects.filter(id = id)
    return render(request,'blog-single.html',views)




def contact(request):
    if request.method == 'POST':
        na = request.POST['name']
        em = request.POST['email']
        sub = request.POST['subject']
        mes = request.POST['message']
        data = Contact.objects.create(
            name = na,
            email = em,
            subject = sub,
            message = mes
        )
        data.save()

    return render(request,'contact.html')



def about(request):
    return render(request,'about.html')

def category_view(request, category_name):
    category = Category.objects.get(name=category_name)
    blogs = Blog.objects.filter(category=category)

    context = {
        'blogs': blogs,
        'category': category,
    }
    return render(request, 'category.html', context)


def search_view(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query', '')

        # Perform the search query on the Blog model
        blogs = Blog.objects.filter(title__icontains=search_query)

        context = {
            'search_query': search_query,
            'blogs': blogs
        }
        return render(request, 'search.html', context)


def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_password')
    

        if pass1!=pass2:
            messages.error("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'registration.html')


def loginview(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('contact')
        else:
            messages.error ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
