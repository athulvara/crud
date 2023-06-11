from django.shortcuts import render,redirect,get_object_or_404
from .models import Form
from django.contrib import messages

# Create your views here.
def demo(request):
    task1=Form.objects.all()
    if request.method== 'POST':
        num=request.POST.get('num','')
        name=request.POST.get('name','') 
        desc=request.POST.get('desc','')
        task=Form(num=num,name=name,desc=desc)
        task.save()    
        messages.info(request,'Data created successfully')
    return render(request,'home.html',{'task':task1})

def delete(request,taskid):
    task=Form.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=get_object_or_404(Form,id=id)
    if request.method == 'POST':
        task.num = request.POST.get('num')
        task.name = request.POST.get('name')
        task.desc = request.POST.get('desc')
        task.save()
        return redirect('/')
    return render(request,'update.html',{'task':task})