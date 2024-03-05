from django.shortcuts import render,HttpResponseRedirect
from app1.forms import student_form
from app1.models import Students_model,movies_model
from django.http import JsonResponse

# view for creating instaces of table
def create_row(request):
    context={}
    form=student_form(request.POST)
    if form.is_valid():
        form.save()
    
    context['form']=form
    return render(request,"create_row.html",context)

# view for listing rows of model
def list_rows(request):
    context={}
    context['database']=Students_model.objects.all()

    return render(request,'list_row.html',context)

# # view for checking details of a particular instance
def detail_row(request,id):
    context={}
    context["data"]=Students_model.objects.get(student_Roll=id)
    return render(request,"detail_row.html",context)

# view for updating instances of table
def update_row(request,id):
    context={}
    obj=Students_model.objects.get(student_Roll=id)

    form=student_form(request.POST,instance=obj)  # pass the object as instance in form

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context["form"]=form

    return render(request,"update_row.html",context)

# view for deleting instaces of table
def delete_row(request,id):
    context={}
    obj=Students_model.objects.get(student_Roll=id)

    if request.method=="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    
    return render(request,"delete_row.html",context)

def movie_list(request):
    movies=movies_model.objects.all()
    data={
        'movies':list(movies.values())   # movies.values values of objects in the variable movies
    }
    return JsonResponse(data)  # returning data in the form of json response
def movie_detail(request,id):
    movie=movies_model.objects.get(movie_name=id)
    data={
        'name':movie.movie_name,
        'description':movie.movie_description,
        'active':movie.movie_active
    }
    return JsonResponse(data)