from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from .models import User
from django.template import loader

from polls.form import UserForm  
def index(request):  
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('authentificated')
            except:  
                HttpResponseNotFound("Cant find page")
    else:  
        form = UserForm()  
    return render(request,'polls/index.html',{'form':form})  
def authentificated(request):  
    users = User.objects.all()  
    return render(request,"polls/authentificated.html",{'users':users})  
def edit(request,user_id):  
    user = User.objects.get(pk=user_id)  
    return render(request,"polls/edit.html", {'user':user})  
def update(request,user_id):  
    user = user.objects.get(pk=user_id)  
    form = UserForm(request.POST,instance = user)  
    if form.is_valid():  
        form.save()  
        return redirect('authentificated')  
    return render(request, "polls/edit.html", {'user': user})  

def remove(request,user_id):  
    user = User.objects.get(pk=user_id)  
    user.delete()
    print(id)
    return redirect('authentificated')