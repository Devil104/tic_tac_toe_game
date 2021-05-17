from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.decorators import login_required





@login_required
def deshboardviews(request):
    return render(request, 'deshboard.html')

def game1(request):
    return render(request, 'login/game.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')


    else:
        form = UserCreationForm()



    return render(request, 'login/registration.html',{'form':form})


