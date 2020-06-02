from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
@xframe_options_exempt
def index(request):
    context_dict = {}
    return render(request, 'ndt/index.html', context_dict)

@xframe_options_exempt
def about(request):
    context_dict = {}
    return render(request, 'ndt/about.html', context_dict)

@xframe_options_exempt
def contact(request):
    context_dict = {}
    return render(request, 'ndt/contact.html', context_dict)

@xframe_options_exempt
def services(request):
    context_dict = {}
    return render(request, 'ndt/services.html', context_dict)

@xframe_options_exempt
def training(request):
    context_dict = {}
    return render(request, 'ndt/training.html', context_dict)

@xframe_options_exempt
def careers(request):
    context_dict = {}
    return render(request, 'ndt/careers.html', context_dict)

@xframe_options_exempt
def mission(request):
    context_dict = {}
    return render(request, 'ndt/mission.html', context_dict)

