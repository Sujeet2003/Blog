from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import facts, posts, logginedUser, projectItems, personalDetails, personalSkills
from django.contrib import messages
from .forms import updateFact, updatePost, updateUserComments
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def home(request):
    message = "Posts Is Not Available For This Query"
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    if query:
        Posts = posts.objects.filter(
            Q(post_title__icontains=query)
        )[0:3]
    else:
        Posts = posts.objects.all().order_by('-post_created').filter()[0:3]

    Facts = facts.objects.all().filter()[0:3]

    context = {
        'message': message,
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
            messages.error(request, "Enter the valid inputs!!")
    else:
        return render(request, 'createFact.html', {'form': form})
    

def deleteFacts(request, pk):
    fact = facts.objects.get(id=pk)
    name = fact.fact_title
    if request.method == 'POST':
        fact.delete()
        messages.error(request, "Fact has been deleted successfully!!")
        return redirect('facts')
    else:
        return render(request, 'delete.html', {'name': name})

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
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username/Password in invalid, Try again!!")
            return redirect('login')
    else:
        return render(request, 'userRegister.html')

def userLogout(request):
    logout(request)
    return redirect('home')

def post(request):
    message = "Posts Is Not Available For This Query"
    users = logginedUser.objects.all().filter()[0:10]
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    if query:
        total_post = posts.objects.filter(
            Q(post_title__icontains=query)
        )
    else:
        message = ""
        total_post = posts.objects.all().order_by('-post_created').filter()[0:30]

    context = {
        'total_post': total_post,
        'users': users,
        'message': message,
    }
    return render(request, 'post.html', context)


@login_required(login_url='login')
def displayPost(request, pk):
    post = posts.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'displayPost.html', context)


def uploadPost(request):
    page = 'upload'
    if request.method == 'POST':
        post_title = request.POST['post_title']
        post_problem = request.POST['post_problem']
        post_image = request.FILES.get('post_image', None)
        post_description = request.POST['post_description']
        post = posts(post_title=post_title, post_problem=post_problem, post_image=post_image, post_description=post_description)
        post.save()
        messages.success(request, "Post has been uploaded successfully!!")
        return redirect('post')
    else:
        return render(request, 'uploadPost.html', {'page': page})

def updatePosts(request, pk):
    update_post = posts.objects.get(id=pk)
    form = updatePost(instance=update_post)
    if request.method == 'POST':
        form = updatePost(request.POST, instance=update_post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post has been updated successfully!!")
            return redirect('post')
        else:
            form = updatePost(instance=update_post)
    else:
        return render(request, 'uploadPost.html', {'update_form': form, 'update_post': update_post})
    
def deletePosts(request, pk):
    post = posts.objects.get(id=pk)
    name = post.post_title
    if request.method == 'POST':
        post.delete()
        messages.error(request, "Post has been deleted successfully!!")
        return redirect('post')
    else:
        return render(request, 'delete.html', {'name': name})
    
def askQuery(request):
    if request.method == 'POST':
        user_query = request.POST['user_query']
        comment = logginedUser(user=request.user, user_query=user_query)
        comment.save()
        messages.success(request, "Thanks for your comment, we'll review it soon!!")
        return redirect('post')
    else:
        return render(request, 'post.html')
    
def updateComments(request, pk):
    update_post = logginedUser.objects.get(id=pk)
    post = updateUserComments(instance=update_post)
    if request.method == 'POST':
        post = updateUserComments(request.POST, instance=update_post)
        if post.is_valid():
            post.save()
            messages.success(request, "Comment has been updated successfully!!")
            return redirect('post')
        else:
            post = updateUserComments(instance=update_post)
    else:
        return render(request, 'comments.html', {'post': post, 'update_post': update_post})
    
def deleteComments(request, pk):
    comment = logginedUser.objects.get(id=pk)
    name = comment.user
    if request.method == 'POST':
        comment.delete()
        messages.error(request, "Comment has been deleted successfully!!")
        return redirect('post')
    else:
        return render(request, 'delete.html', {'name': name})
    
def about(request):
    projects = projectItems.objects.all()
    details = personalDetails.objects.get()
    skills = personalSkills.objects.get()
    context = {
        'projects': projects,
        'details': details,
        'skills': skills,
    }
    return render(request, 'about.html', context)