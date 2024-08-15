from django.shortcuts import render, redirect

from article.models import Jurnal, Band, Member, User
from article.forms import MemberForm, JurnalForm, UserForm


def user_index(request):
    obj = User.objects.all().order_by("id")

    return render(request, 'user_index.html', {"objects": obj})    

def user_create(request):
    if request.method=="POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        age = request.POST.get("age")

        User.objects.create(name=name, surname=surname, age=age)

        return redirect("/users/")

    return render(request, 'user_create.html')

def user_detail_view(request, pk):
    obj = User.objects.get(id=pk) 

    form = UserForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()

        return redirect('/users/')
    
    context = {
        "obj": obj,
        "form": form,
    }

    return render(request, 'user_detail.html', context)

def user_delete(request, pk):
    obj = User.objects.get(id=pk)

    obj.delete()

    return redirect('/users/')

def index(request):
    obj = Jurnal.objects.all().order_by("id")
    
    return render(request, 'index.html', {"objects": obj})

def data_create(request):
    if request.method=="POST":
        name = request.POST.get("name")
        baho = request.POST.get("baho")
        
        Jurnal.objects.create(student=name, baho=baho)

        return redirect("index")

    return render(request, 'data_create.html')

def detail_view(request, pk):
    obj = Jurnal.objects.get(id=pk) 

    form = JurnalForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()

        return redirect('/index/')
    
    context = {
        "obj": obj,
        "form": form,
    }

    return render(request, 'detail.html', context)

def jurnal_delete(request, pk):
    obj = Jurnal.objects.get(id=pk)
    
    obj.delete()
    
    return redirect('index')

def band_list(request):
    obj = Band.objects.all().order_by("id")

    if request.method == 'POST':
        name = request.POST.get('name')

        Band.objects.create(name=name)

        return redirect('bands')

    return render(request, 'band.html', {'bands': obj})

def member_create(request):
    members = Member.objects.all().order_by("id")

    form = MemberForm(request.POST or None)
    
    if form.is_valid():
        form.save()

        return redirect("members")
    
    context = {
        'form':form,
        'members': members,
    }
    
    return render(request, 'member_create.html', context)
