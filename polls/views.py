from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import User
from django.template import loader

from polls.form import UserForm  
def index(request):  
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('polls/authentificated')  
            except:  
                pass  
    else:  
        form = UserForm()  
    return render(request,'polls/index.html',{'form':form})  
def authentificated(request):  
    users = User.objects.all()  
    return render(request,"polls/authentificated.html",{'users':users})  
def edit(request, id):  
    user = User.objects.get(id=id)  
    return render(request,'edit.html', {'user':user})  
def update(request, id):  
    user = user.objects.get(id=id)  
    form = UserForm(request.POST, instance = user)  
    if form.is_valid():  
        form.save()  
        return redirect("/authentificated/")  
    return render(request, 'edit.html', {'user': user})  
def remove(request, id):  
    user = user.objects.get(id=id)  
    user.delete()  
    return redirect("/authentificated/")  