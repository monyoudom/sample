from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import InformaitonForms

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = InformaitonForms(request.POST)
        form.save()
        return HttpResponseRedirect('polls/thanks/')
    else:
        form = InformaitonForms()
    return render(request, 'index.html', {'form': form})
        


def thanks(request):
    return render(request, 'thank.html')