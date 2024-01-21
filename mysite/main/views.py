from django.shortcuts import render, get_object_or_404, redirect
from .models import Zapis
from .forms import Create

def home(request):
    return render(request, 'main/home.html')

def view(request):
    return render(request, 'main/view.html', {'zapisi':Zapis.objects.order_by('-id')})

def view_zapis(request, id):
    return render(request, 'main/view_detail.html', {'zapis':get_object_or_404(Zapis, id=id)})

def create(request):
    if request.method == "POST":
        form = Create(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request, 'main/create.html', {'form': Create})