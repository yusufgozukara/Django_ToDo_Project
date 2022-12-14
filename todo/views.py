
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

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
            messages.success(request, 'Başarıyla Eklendi')
            return redirect('home')

    context = {
        "form" : form
    }

    return render(request, 'todo/todo_add.html', context)

def todo_update(request,id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {
        'todo' : todo,
        'form' : form
    }
    return render(request, 'todo/todo_update.html', context)

def todo_delete(request,id):
    todo = Todo.objects.get(id=id)

    if request.method == 'POST':
        todo.delete()
        messages.warning(request, 'Başarıyla Silindi')
        return redirect('home')

    context = {
        'todo' : todo
    }

    return render(request, 'todo/todo_delete.html', context)