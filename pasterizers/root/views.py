from django.shortcuts import render
from .forms import ParameterForm


def index(request):
    return render(request, 'root/index.html')


def pet4(request):
    submitbutton = request.POST.get('submit')
    form = ParameterForm(request.POST or None)
    if form.is_valid():
        day = form.cleaned_data.get('day')
        params = form.cleaned_data.get('parameters')
        print('=================')
        print(params)
        context = {
            'form': form,
            'result': day,
            'submitbutton': submitbutton,
        }
        return render(request, 'root/PET-4.html', context)
    return render(request, 'root/PET-4.html', {'form': form}) 


def glass6(request):
    return render(request, 'root/GLASS-6.html')       


def can1(request):
    return render(request, 'root/CAN-1.html')       


def pet2(request):
    return render(request, 'root/PET-2.html')


def petkeg(request):
    return render(request, 'root/PET-KEG.html')


def keg(request):
    return render(request, 'root/KEG.html')


def help(request):
    return render(request, 'root/help.html')


def contacts(request):
    return render(request, 'root/contacts.html')


def review(request):
    return render(request, 'root/review.html')
