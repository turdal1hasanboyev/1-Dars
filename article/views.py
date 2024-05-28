from django.shortcuts import render, redirect
from .models import Jurnal, Band, Member, User
from .forms import MemberForm, JurnalForm, UserForm


def user_index(request):
    obj = User.objects.all()
    context = {
        "objects": obj
    }

    return render(request, 'user_index.html', context)    

def user_create(request):
    if request.method=="POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        age = request.POST.get("age")
        obj = User.objects.create(name=name, surname=surname, age=age)

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
        "form": form
    }

    return render(request, 'user_detail.html', context)

def user_delete(request, pk):
    obj = User.objects.get(id=pk)
    obj.delete()

    return redirect('/users/')

def index(request):
    obj = Jurnal.objects.all()

    context = {
        "objects": obj
    }
    
    return render(request, 'index.html', context)

def data_create(request):
    if request.method=="POST":
        name = request.POST.get("name")
        baho = request.POST.get("baho")
        obj = Jurnal.objects.create(student=name, baho=baho)

        return redirect("/")

    return render(request, 'data_create.html')

def detail_view(request, pk):
    obj = Jurnal.objects.get(id=pk) 

    form = JurnalForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

        return redirect('/')
    
    context = {
        "obj": obj,
        "form": form
    }

    return render(request, 'detail.html', context)

def jurnal_delete(request, pk):
    obj = Jurnal.objects.get(id=pk)
    obj.delete()
    return redirect('/')

def band_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        Band.objects.create(name=name)

        return redirect('bands')
    
    obj = Band.objects.all()

    return render(request, 'band.html', {'bands': obj})

def member_create(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect("members")
    
    members = Member.objects.all()
    
    context = {
        'form':form,
        'members': members
    }
    
    return render(request, 'member_create.html', context)
