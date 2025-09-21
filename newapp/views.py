from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        form_1 = pipe_inspection(request.POST, request.FILES)
        if form_1.is_valid():
            form_1.save()
            messages.success(request, "Form submitted successfully")
            return redirect('index')  # redirect to the same page
        else:
            messages.error(request, "Form is not valid. Please check the fields.")
    else:
        form_1 = pipe_inspection()

    return render(request, 'index.html', {'form': form_1})

def new_data(request, id=id):
    data_submitted = ghd_pipe_inspection.objects.all()
    return render(request, 'data.html', context={'data': data_submitted})