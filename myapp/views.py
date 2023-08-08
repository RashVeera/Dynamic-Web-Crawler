from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect
# Create your views here.

def scrape(request):
    
    if request.method=='POST':
        site=request.POST.get('site','')
        page=requests.get(site)
        soup=BeautifulSoup(page.text,'html.parser')
        for links in soup.find_all('a'):
            link_address=links.get('href')
            link_name=links.string
            Link.objects.create(address=link_address,name=link_name)
        return HttpResponseRedirect('/')
    else:
        data=Link.objects.all()
    
    return render(request,'myapp/index.html',{'data':data})


def clear(request):
    Link.objects.all().delete()
    return render(request,'myapp/index.html')