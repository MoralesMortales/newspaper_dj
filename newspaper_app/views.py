from django.contrib import auth
from django.shortcuts import get_object_or_404, redirect, render
from .models import newspaper_db
from .forms import newNewspaper_form  

# Create your views here.
def mainView(request):
    info = newspaper_db.objects.all()
    return render(request, 'main.html', {'news': info})

def createNew(request):
    if request.method == 'POST':
        form = newNewspaper_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    else:
        form = newNewspaper_form()

    return render(request, 'create.html',  {'form': form})

def deleteOne(request, id):
    newspaper = get_object_or_404(newspaper_db, id=id)

    if request.method == 'POST':
        newspaper.delete()
        return redirect('main')


def chooseToDelete(request):
    info = newspaper_db.objects.all()
    return render(request, 'delete.html', {'news': info})

def chooseToEdit(request):
    info = newspaper_db.objects.all()
    return render(request, 'edit.html', {'news': info})


def editing(request, id):
    newspaper = get_object_or_404(newspaper_db, id=id)
    form = newNewspaper_form(instance=newspaper)

    if request.method == 'POST':
        form = newNewspaper_form(request.POST, instance=newspaper)
        if form.is_valid():
            form.save()
            return redirect('main')  # Redirect after successful save
        else:
            print(form.errors)  # Print errors to console for debugging

    return render(request, 'editing.html', {'form': form, 'id': id})

