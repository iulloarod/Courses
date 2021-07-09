from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from django.contrib import messages

def index(request):
    course_info= Course.objects.all()
    if request.method =="GET":
        context={
            "all_courses": course_info,
        }
        return render(request, 'index.html', context)
    errors = Course.objects.add_course_val(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    else:
        if request.method == "POST":
            Course.objects.create(name=request.POST['name'], 
                                description= request.POST['description']
                                )
            messages.success(request, "Course successfully created")
            return redirect("/")


def delete(request, id):
    course_info = Course.objects.get(id=int(id))
    if request.method=='GET':
        context = {
            "id": course_info.id,
            "name": course_info.name,
            "description": course_info.description,
        }
        return render(request,"delete.html", context)
    if request.method=='POST':
        if request.POST['no'] == True:
            return redirect("/")
        else:
            pass
        if request.POST['yes'] == True:
            course_info.delete()
        return redirect("/")