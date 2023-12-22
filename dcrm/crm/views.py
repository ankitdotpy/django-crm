from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    context = {
        'title': 'Home'
    }

    if request.method == 'POST':
        context['title'] = 'Log In'
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have been logged in. Redirecting to home...')
            return redirect('home')
        else:
            messages.error(request,'There was an error logging in. Please try again...')
            return redirect('home')
    else:
        return render(request,'crm/home.html',context)

def logout_user(request):
    logout(request)
    messages.success(request,'You have been logged out...')
    return redirect('home')