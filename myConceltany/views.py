from django.shortcuts import render,redirect
from .models import User
from .forms import formUser

def myHomeView(request):
    obj = User.objects.all()
    context = {
        # Add context data here if needed
        'obj' : obj,
    }
    return render(request, 'index.html', context)
def showFormViews(request):
    if request.method == 'POST':
        form = formUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success URL
    else:
        form = formUser()
    context = {
        'form': form
    }
    return render(request, 'home.html', context)
def success(request):
    context = {}
    return render(request, 'SuccessSull.html', context)