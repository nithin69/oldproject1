from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .models import *
from .forms import *
from booking.models import *
##from reservations.models import *
from django.db.models import Q
##from myproject.forms import *
##from django.core.paginator import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt



@xframe_options_exempt
def index(request):
    
    events = Events.objects.all().order_by('-id')
    news = News.objects.all().order_by('-id')
    carosuel = Carosuel.objects.all().order_by('id')
    youtube = Youtube.objects.all().order_by('-id')
    marquee = Marquee.objects.all().order_by('-id')
    context_dict = {'marquee':marquee, 'Events' : events, 'news' : news, 'Carosuel' : carosuel, 'Youtube' : youtube}
    return render(request, 'index.html', context_dict)

@xframe_options_exempt
def events(request):
    events = Events.objects.all().order_by('-id')
    context_dict = {'Events' : events}
    return render(request, 'events.html', context_dict)


@xframe_options_exempt
def news(request):
    news = News.objects.all().order_by('-id')
    context_dict = {'News' : news}
    return render(request, 'news.html', context_dict)


@xframe_options_exempt
def jobs(request):
    jobs = Jobs.objects.all().order_by('-id')
    context_dict = {'Jobs' : jobs}
    return render(request, 'jobs.html', context_dict)
@xframe_options_exempt
def scolarship(request):
    scolarship = Scolarship.objects.all().order_by('-id')
    context_dict = {'Scolarship' : scolarship}
    return render(request, 'scolarship.html', context_dict)
@xframe_options_exempt
def about(request):
    context_dict = {}
    return render(request, 'about.html', context_dict)
@xframe_options_exempt
def activites(request):
    activites = Activites.objects.all().order_by('-id')
    context_dict = {'Activites' : activites}
    return render(request, 'activites.html', context_dict)
@xframe_options_exempt
def contact(request):
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        print "contact_form  :", contact_form
        #print "request post : ", request.POST
        if contact_form.is_valid():
            con = contact_form.save()
            done = True
        else:
            "sorry "
            print contact_form.errors
    else:
        contact_form = ContactForm()
    return render_to_response('contact.html', {'contact_form': contact_form, 'done': done}, context)

##    context_dict = {}
##    return render(request, 'contact.html', context_dict)
@xframe_options_exempt
def founder(request):
    context_dict = {}
    return render(request, 'founder.html', context_dict)
@xframe_options_exempt
def secretery(request):
    secretery = Secretery.objects.all().order_by('-id')
    context_dict = {'Secretery' : secretery}
    return render(request, 'secretery.html', context_dict)
@xframe_options_exempt
def faq(request):
    context_dict = {}
    return render(request, 'faq.html', context_dict)
@xframe_options_exempt
def image(request):
    image = Image.objects.all().order_by('-id')
    context_dict = {'image' : image}
    return render(request, 'image.html', context_dict)
@xframe_options_exempt
def video(request):
    video = Video.objects.all().order_by('-id')
    context_dict = {'video' : video}
    return render(request, 'video.html', context_dict)
@xframe_options_exempt
def audio(request):
    audio = Audio.objects.all().order_by('-id')
    context_dict = {'audio' : audio}
    return render(request, 'audio.html', context_dict)
@xframe_options_exempt
def hallbooking(request):
    context_dict = {}
    return render(request, 'hallbooking.html', context_dict)
@xframe_options_exempt
def members(request):
    members = Members.objects.all().order_by('id')
    context_dict = {'Members' : members}
    return render(request, 'members.html', context_dict)
@xframe_options_exempt
def roombooking(request):
    context_dict = {}
    return render(request, 'roombooking.html', context_dict)
@xframe_options_exempt
def searchbook(request):
    Library = library.objects.all().order_by('-id')
    context_dict = {'library' : Library}
    return render(request, 'searchbook.html', context_dict)
@xframe_options_exempt
def websites(request):
    context_dict = {}
    return render(request, 'websites.html', context_dict)


@xframe_options_exempt
def search(request):
    context = RequestContext(request)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    print q
    
    search = Members.objects.filter(Q(name = q)| Q(membership = q)).order_by('-id')
    print search
    return render_to_response('searchmembers.html', {'search' : search, 'category': q}, context)

@xframe_options_exempt
def search2(request):
    context = RequestContext(request)
    if 'r' in request.GET and request.GET['r']:
        r = request.GET['r']
    print r
    
    search2 = library.objects.filter(Q(book = r)| Q(author = r)).order_by('-id')
    print search2
    return render_to_response('searchb.html', {'search2' : search2, 'category': r}, context)


@xframe_options_exempt
@csrf_exempt
def sms(request):
    conn = MySQLdb.connect("localhost","root","1234","ambedkar" )
    sqlcursor = conn.cursor() 
    sqlcursor.execute("SELECT name,phone FROM ambedkar.ams_members")
    row = sqlcursor.fetchall()
    
    authkey = "144560AtNwgJSU58c2e32e"
    url = "http://sms.rpsms.in/api/sendhttp.php"

    for message in row:
        mobiles = message[1]
        sms = request.POST.get('sms')
        message1 = request.GET['message']
        print message1
        sender = "ambdkr" 
        route = 1 
        # Prepare you post parameters
        values = {
                  'authkey' : authkey,
                  'mobiles' : mobiles,
                  'message' : message1,
                  'sender' : sender,
                  'route' : route
                  }

    postdata = urllib.urlencode(values) # URL encoding the data here.
    req = urllib2.Request(url, postdata)
    response = urllib2.urlopen(req)
    output = response.read()
    context_dict = {}
    return render(request,'sms.html', context_dict)


