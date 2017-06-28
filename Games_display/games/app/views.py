from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from app.models import gamelist
# Create your views here.

class Myregistration(RegistrationView):
    def get_success_url(self,request):
        return '/games/'

def home(request):
    if (request.user.is_authenticated()):
        return render(request,'home.html')
    return login(request,template_name='home.html')

@login_required(login_url = '/games/accounts/login/')
def profile(request):
    return render(request,template_name = 'profile.html')


@login_required(login_url = '/games/accounts/login/')
def gamelist_view(request):


    all_games_set = gamelist.objects.all().values_list('title')	
    all_games = [i[0].encode("utf8") for i in all_games_set]	

    game_list = gamelist.objects.all().order_by('-score')
    page = request.GET.get('page',1)
    paginator = Paginator(game_list,15)
    
    try:
	list_games = paginator.page(page)
    except PageNotAnInteger:
	list_games = paginator.page(1)
    except EmptyPage:
	list_games = paginator.page(paginator.num_pages)

    return render(request,'gamelist.html',{'listofgames':list_games,'flag':'all','allgames':all_games})

@login_required(login_url = '/games/accounts/login/')
def contact(request):
    return render(request,template_name = 'contact.html')


@login_required(login_url = '/games/accounts/login/')
def eachgameview(request,gameid):
    game_details = dict()
    game_info = gamelist.objects.all().filter(id = gameid)
    game_details['info'] = game_info
    return render(request,'eachgame.html',{'gameinfo':game_details})


@login_required(login_url = '/games/accounts/login/')
def platform(request,pid):
    platforms_set = list(set(gamelist.objects.all().values_list('platform')));
    platforms = [i[0] for i in platforms_set]

    all_games_set = gamelist.objects.all().values_list('title')	
    all_games = [i[0].encode("utf8") for i in all_games_set]	

    platform_current = platforms[int(pid)-1]
    #print platform_current
    games_to_platform = gamelist.objects.all().filter(platform = platform_current).order_by('-score')
    page = request.GET.get('page',1)
    paginator = Paginator(games_to_platform,15)
    
    try:
	list_games = paginator.page(page)
    except PageNotAnInteger:
	list_games = paginator.page(1)
    except EmptyPage:
	list_games = paginator.page(paginator.num_pages)

    return render(request,'gamelist.html',{'listofgames':list_games,'flag':'platform','platforms':platforms,'allgames':all_games,'cur_platform':platform_current})


@login_required(login_url = '/games/accounts/login/')
def genre(request,gid):

    all_games_set = gamelist.objects.all().values_list('title')	
    all_games = [i[0].encode("utf8") for i in all_games_set]	


    genre_set = list(set(gamelist.objects.all().values_list('genre')));
    genres = [i[0] for i in genre_set]

    genre_current = genres[int(gid)-1]
    games_to_genres= gamelist.objects.all().filter(genre = genre_current).order_by('-score')

    page = request.GET.get('page',1)
    paginator = Paginator(games_to_genres,15)
    
    try:
	list_games = paginator.page(page)
    except PageNotAnInteger:
	list_games = paginator.page(1)
    except EmptyPage:
	list_games = paginator.page(paginator.num_pages)

    return render(request,'gamelist.html',{'listofgames':list_games,'flag':'genre','genres':genres,'allgames':all_games,'cur_genre':genre_current})


