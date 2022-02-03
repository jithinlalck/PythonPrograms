from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('classbasedViewHome')

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('classbasedDetailView',kwargs={'pk':self.object.id})

class TaskListview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task'

class TaskDetailview(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name = 'task'


# Create your views here.

def fn_add(request):
    task_obj1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('txtName','')
        priority=request.POST.get('txtPriority', '')
        date = request.POST.get('txtDate', '')
        task_obj=Task(name=name,priority=priority,date=date)
        task_obj.save()
        return redirect('/')
    return render(request,'home.html',{'task': task_obj1})

# def fn_details(request):
#     task_obj=Task.objects.all()
#     return render(request,'details.html',{'task':task_obj})

def fn_delete(request,taskid):
    task_obj = Task.objects.get(id=taskid)
    if request.method=='POST':
        task_obj.delete()
        return redirect('/')
    return render(request,'delete.html')

def fn_update(request,taskid):
    task_obj=Task.objects.get(id=taskid)
    form_obj=TaskForm(request.POST or None,instance=task_obj)
    if form_obj.is_valid():
        form_obj.save()
        return redirect('/')
    return render(request,'edit.html', {'fobj':form_obj, 'tobj':task_obj})
