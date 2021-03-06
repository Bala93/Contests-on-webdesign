from django.shortcuts import render
from app.models import Matchinfo
from django.db.models import Q
from datetime import datetime

# Create your views here.

def ipl_home(request):
	
	return render(request,'ipl_home.html')

def team_home(request,teamno):
	team_id = {'1':'Chennai Super Kings','2':'Delhi Daredevils','3':'Kolkata Knight Riders','4':'Mumbai Indians','5':'Pune Warriors','6':'Kings XI Punjab','7':'Rajasthan Royals','8':'Royal Challengers Bangalore','9':'Gujarat Lions','10':'Deccan Chargers','11':'Sunrisers Hyderabad','12':'Rising Pune Supergiants','13':'Kochi Tuskers Kerala'}
	team_name = team_id[teamno]

	seasons_played_set = set(Matchinfo.objects.filter(Q(team1 = team_name) or Q(team2 = team_name)).values_list('season'))

	seasons_played  = [int(i[0]) for i in seasons_played_set]
	print seasons_played
	seasons_played.sort()
	
	return render(request,'team_home.html',{'seasons':seasons_played,'teamno':teamno,'teamname':team_name})	

def seasons(request,teamno,season):
	
	team_id = {'1':'Chennai Super Kings','2':'Delhi Daredevils','3':'Kolkata Knight Riders','4':'Mumbai Indians','5':'Pune Warriors','6':'Kings XI Punjab','7':'Rajasthan Royals','8':'Royal Challengers Bangalore','9':'Gujarat Lions','10':'Deccan Chargers','11':'Sunrisers Hyderabad','12':'Rising Pune Supergiants','13':'Kochi Tuskers Kerala'}
	team_name = team_id[teamno]
	
	fixtures = Matchinfo.objects.filter((Q(team1 = team_name) | Q(team2 = team_name)) & Q(season = season))
	
	team_battle = []
	for each in fixtures:
		date_t = [int(i) for i in each.date.split('-')]
		date_in = datetime(date_t[0],date_t[1],date_t[2])
	
		date_info = date_in.strftime("%A %d, %B %Y")
			
		cont = "%s vs %s at %s on %s"%(each.team1,each.team2,each.city,date_info)
		team_battle.append({'matchno':each.id,'battle':cont})

	return render(request,'seasons.html',{'fixtures':team_battle,'teamno':teamno,'season':season,'teamname':team_name})

def matchinfo(request,teamno,season,matchno):

	
	team_id = {'1':'Chennai Super Kings','2':'Delhi Daredevils','3':'Kolkata Knight Riders','4':'Mumbai Indians','5':'Pune Warriors','6':'Kings XI Punjab','7':'Rajasthan Royals','8':'Royal Challengers Bangalore','9':'Gujarat Lions','10':'Deccan Chargers','11':'Sunrisers Hyderabad','12':'Rising Pune Supergiants','13':'Kochi Tuskers Kerala'}
	
	team_name = team_id[teamno]

	matchdetails = Matchinfo.objects.filter(id = matchno)

	
	
	return render(request,'matches.html',{'matchinfo':matchdetails})

