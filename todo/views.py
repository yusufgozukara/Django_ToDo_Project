
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.

def home(request):
    todos = Todo.objects.all()
    form = TodoForm
    # if request.method == 'POST':
    #     form = TodoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    #submit yapınca bilgiyi göndermesi için ya create'deki bu metodu buraya taşımak 
    #ya da kopyalamak gerekir. ya da formun action kısmına /add/ yazıp oraya istek gönderebiliriz. 

    context = {
        'todos' : todos,
        'form' : form
    }

    return render(request, 'todo/home.html', context)

def todo_create(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        "form" : form
    }

    return render(request, 'todo/todo_add.html', context)
