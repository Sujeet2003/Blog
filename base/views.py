from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import facts, posts
from django.contrib import messages
from .forms import updateFact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    Facts = facts.objects.all().filter()[0:3]
    Posts = posts.objects.all().order_by('-post_created').filter()[0:7]
    context = {
        'facts': Facts,
        'Posts': Posts,
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def allFacts(request):
    all_facts = facts.objects.all()
    context = {
        'all_facts': all_facts,
    }
    return render(request, 'facts.html', context)


def createFacts(request):
    page = 'create'
    if request.method == 'POST':
        fact_title = request.POST['fact_title']
        fact_fact = request.POST['fact_fact']
        fact_consideration = request.POST['fact_consideration']
        form = facts(fact_title=fact_title, fact_fact=fact_fact, fact_consideration=fact_consideration)
        form.save()
        messages.success(request, "Fact has been created successfully!!")
        return redirect('createFacts')
    else:
        return render(request, 'createFact.html', {'page': page})
def updateFacts(request, pk):
    fact = facts.objects.get(id=pk)
    form = updateFact(instance=fact)
    if request.method == 'POST':
        form = updateFact(request.POST, instance=fact)
        if form.is_valid():
            form.save()
            messages.success(request, "Fact has been updated successfully!!")
            return redirect('facts')
    else:
        return render(request, 'createFact.html', {'form': form})
    

def deleteFacts(request, pk):
    fact = facts.objects.get(id=pk)
    fact.delete()
    messages.info(request, "Fact has been deleted successfully!!")
    return redirect('facts')

def userRegister(request):
    page = 'user_register'
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists!!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists!!")
                return redirect('register')
            else:
                register = User.objects.create_user(username=username, email=email, password=password1)
                register.save()
                messages.success(request, "Registered successfully!!")
                return redirect('login')
        else:
            messages.info(request, "Password mis-matched, Try again!!")
            return redirect('register')
    else:
        return render(request, 'userRegister.html', {'page': page})

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'userRegister.html')

def userLogout(request):
    logout(request)
    return redirect('home')

def post(request):
    total_post = posts.objects.all().order_by('-post_created')
    context = {
        'total_post': total_post
    }
    return render(request, 'post.html', context)


def displayPost(request, pk):
    post = posts.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'displayPost.html', context)