from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from app.forms import UploadFileForm
# Create your views here.
from django.http import JsonResponse


class Myregistration(RegistrationView):
    def get_success_url(self,request):
        return '/lynk/'

def home(request):
    if (request.user.is_authenticated()):
	#form = UploadFileForm
	results = [{"teamname":"Goldenratio","imageuid":23,"name":"abinaya"},{"teamname":"Goldenratio","imageuid":25,"name":"abinaya"},{"teamname":"Goldenratio","imageuid":30,"name":"abinaya"}]
        return render(request,'home.html',{'results':results})
    return login(request,template_name='home.html')


@login_required(login_url = '/lynk/accounts/login/')
def profile(request):
    return render(request,template_name = 'profile.html')


@login_required(login_url = '/lynk/accounts/login/')
def contact(request):
    return render(request,template_name = 'contact.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
	#print (form)
        if form.is_valid():
	    print ("Hai")
            pred_data = handle_uploaded_file(request.FILES['file'])
            return JsonResponse(pred_data,safe=False)
	 
    return JsonResponse(['Error'],safe=False)

def handle_uploaded_file(f):
    res = ["IN"]
    return res
