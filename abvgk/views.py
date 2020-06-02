from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
@xframe_options_exempt
def index(request):
    context_dict = {}
    return render(request, 'abvgk/index.html', context_dict)

@xframe_options_exempt
def contact(request):
    context_dict = {}
    return render(request, 'abvgk/contact.html', context_dict)

@xframe_options_exempt
def schedule(request):
    context_dict = {}
    return render(request, 'abvgk/schedule.html', context_dict)
