

# Create your views here.
from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    views = {}
    views['blogs'] = Blog.objects.all()
    return render(request,'home.html',views)

def login_view(request):
    return render(request,'login.html')
def register_view(request):
    return render(request,'registration.html')

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