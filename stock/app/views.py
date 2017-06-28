from django.shortcuts import render,redirect
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from stock.settings import BASE_DIR
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from registration.backends.simple.views import RegistrationView
from app.models import companynames,compinfo
from googlefinance import getQuotes
from django.template import RequestContext
import json
# Create your views here.

class Myregistration(RegistrationView):
    def get_success_url(self,request):
        return '/stock/'

def home(request):
    if (request.user.is_authenticated()):
        return render(request,'home.html')
    return login(request,template_name='home.html')

@login_required(login_url = '/stock/accounts/login/')
def profile(request):
    return render(request,template_name = 'profile.html')

#@login_required(login_url = '/stock/accounts/login/')
def company_list(request):
    
    list_comp =  companynames.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(list_comp,25)

    try:
        comp_list = paginator.page(page)
    except PageNotAnInteger:
        comp_list = paginator.page(1)
    except EmptyPage:
        comp_list = paginator.page(paginator.num_pages)

    return render(request,'companylist.html',{'company_list':comp_list})

@csrf_exempt
#@login_required(login_url = '/stock/accounts/login/')
def recent_stock(request,sym):

    company_info = companynames.objects.all().filter(id=sym)
    if request.is_ajax() and request.POST:

        sym = request.POST


        stock_symbol = str(company_info[0].symbol)
        stock_info  = getQuotes(stock_symbol)[0]

        tradetime   = stock_info['LastTradeDateTimeLong']
        tradeprice  = stock_info['LastTradePrice']
        cc = compinfo(symbol = stock_symbol , tradetime = tradetime , tradeprice = tradeprice)
        cc.save()
        msg = tradetime+'  '+tradeprice
        
	print tradeprice 
        return HttpResponse(msg)
    
    return render(request,'viewer.html',{'info':company_info})

  
