from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import URL
import string,random,datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

# function to create shorten url and save it into the database
def shorten_url(request):
    
    if request.method=="POST":
        orignal_url=request.POST.get('orignal_url')
        existing_url=URL.objects.filter(url=orignal_url).first()
        

        # checking if the shortCode for the given url already exists
        if existing_url :
            
            short_url=request.build_absolute_uri('/')+existing_url.shortCode
            return render(request,'index.html',{'short_url':short_url})
        print(existing_url)
        # if the shortCode doesn't exist then create a new shortCode
        short_code=generate_short_code()
        short_url=request.build_absolute_uri('/')+short_code
        print(short_code)
        URL.objects.create(url=orignal_url,shortCode=short_code,created_at=datetime.datetime.now())
        return render(request,'index.html',{'short_url':short_url})
    print('Coiming out')
    return redirect('index')


# function to generate shortCode
def generate_short_code():
    char=string.ascii_letters+string.digits
    short_code=''.join(random.choice(char) for i in range (5))

    #checking if the shortCode is already assigned to some other url if so then create a new one
    while URL.objects.filter(shortCode=short_code).exists():
        short_code=''.join(random.choice(char) for i in range (5))

    return short_code


# function to redirect users coming from short_url to original_url
def redirect_to_original_url(request,short_url):
    short_code=short_url.split('/')[-1]
    result=URL.objects.get(shortCode=short_code)
    result.access_count=result.access_count + 1 if result.access_count else 1
    result.save()
    return redirect(result.url)