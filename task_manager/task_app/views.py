from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Task
from .forms import TaskForm, RegisterForm

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'task_app/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'task_app/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_app/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_app/add_task.html', {'form': form})

@login_required
def update_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_app/update_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_app/delete_task.html', {'task': task})



def task_list(request):
    tasks = Task.objects.all()  # Get all tasks for now, you can filter it later
    return render(request, 'task_app/task_list.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')