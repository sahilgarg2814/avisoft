from django.shortcuts import render,HttpResponseRedirect
from app1.forms import student_form
from app1.models import Students_model

def create_row(request):
    context={}
    form=student_form(request.POST)
    if form.is_valid():
        form.save()
    
    context['form']=form
    return render(request,"create_row.html",context)

def list_rows(request):
    context={}
    context['database']=Students_model.objects.all()

    return render(request,'list_row.html',context)

def detail_row(request,id):
    context={}
    context["data"]=Students_model.objects.get(student_Roll=id)
    return render(request,"detail_row.html",context)

def update_row(request,id):
    context={}
    obj=Students_model.objects.get(student_Roll=id)

    form=student_form(request.POST,instance=obj)  # pass the object as instance in form

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context["form"]=form

    return render(request,"update_row.html",context)

def delete_row(request,id):
    context={}
    obj=Students_model.objects.get(student_Roll=id)

    if request.method=="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    
    return render(request,"delete_row.html",context)