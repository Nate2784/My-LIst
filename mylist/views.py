from django.shortcuts import render, redirect, get_object_or_404
from .models import userInfo, todo

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = userInfo.objects.all()
        for user in users:
            if username == user.email and password == user.password :
                id = user.id
                return redirect('home', id) 
            else:
                continue

    return render(request, 'login.html')

def register(request):

    if request.method =='POST':
      user_name  = request.POST.get('name')
      user_email  = request.POST.get('email')
      user_password  = request.POST.get('password')
   
      obj = userInfo()
      
      obj.name = user_name
      obj.email =user_email
      obj.password = user_password
      obj.save()
      return redirect('login')
    return render(request, 'register.html')

def home(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        status = request.POST['status']

        obj = todo()
      
        obj.userID = id
        obj.name = name
        obj.description = description
        obj.status = status
        obj.save()
    tasks = todo.objects.filter(userID=id)

    done_tasks = tasks.filter(status='done').count()
    tasks_doing = tasks.filter(status='doing').count()
    tasks_todo = tasks.filter(status='todo').count()

    user = userInfo.objects.filter(id=id).first()
    data={
        'id': id,
        'tasks': tasks,
        'done_tasks':done_tasks,
        'tasks_doing':tasks_doing,
        'tasks_todo':tasks_todo,
        'info':user,
    }
    return render(request, 'index.html', data)

def edit_task(request,id, eid):
    task = get_object_or_404(todo, id=eid)
    

    if request.method == 'POST':

        name = request.POST['name']
        description = request.POST['description']
        status = request.POST['status']

        task.name = name
        task.description = description
        task.status = status

        task.save()

        return redirect('home',id)
    data={
        'id':id,
        'task': task,
    }
    
    return render(request, 'edit.html',data)
    
def delete_task(request, id, did):
    task = get_object_or_404(todo, id=did)

    if request.method == 'POST':
        task.delete()
        return redirect('home', id)
    data={
        'id':id,
        'task': task
    }

    return render(request, 'delete_confirmation.html', data)

