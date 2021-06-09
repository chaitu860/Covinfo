from django.shortcuts import render
from bs4 import BeautifulSoup as bp
from .models import newspoint
import requests
def agr(request):
  #https://www.nbcnews.com/health/coronavirus
  #https://www.9news.com.au/coronavirus
  #https://www.indiatoday.in/coronavirus
  re=requests.get('https://www.indiatoday.in/coronavirus-covid-19-outbreak')
  sp=bp(re.content,'html5lib')
  head2=sp.find_all('div',{'class':"catagory-listing"})
  k=[]
  k1=[]
  k2=[]
  for i in head2:
    im=i.find_all('img')
    k.append(im[0]['src'])
    ini=i.find_all('a')
    
    k2.append(ini[0].find_all(text=True)[0])
    
   
    s="https://www.indiatoday.in/"+ini[0]['href']
    k1.append(s)
  data=[]
  for i in range(len(k1)):
    news= newspoint()
    news.headline=k1[i]
    news.desc=k2[i]
    news.img=k[i]
    news.save()
  re1=requests.get('https://covid19.who.int/')
  sp=bp(re1.text,'html.parser')
  tag=sp('span')

  case=tag[6].contents[0]
  dea=tag[7].contents[0]
  vac=tag[9].contents[0]
  dac=newspoint.objects.all()
  k={"neg":case,"death":dea,"vac":vac,'usd':dac}
  return render(request,"hush.html",k)
# Create your views here.
