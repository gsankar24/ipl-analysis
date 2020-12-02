from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Count, Max, F

from .models import Match

def index(request):
    data = []
    seasons = Match.objects.order_by('season').values_list('season',flat=True).distinct()
    season = request.GET.get('season', None)
    template_name = "index.html"
    if season:
        template_name = "includes/table.html"
    else:
        season = seasons[0]
        
    season_query = Match.objects.filter(season=season)

    top_four_teams = [i['winner'] for i in season_query.values(
                'winner').annotate(the_count=Count('winner')).order_by('-the_count')[:4]]
    max_toss_winning_team = season_query.values(
                'toss_winner').annotate(the_count=Count('toss_winner')).order_by(
                '-the_count')[0]['toss_winner']
    max_player_of_match_winner =  season_query.values(
                'player_of_match').annotate(the_count=Count('player_of_match')).order_by(
                '-the_count')[0]['player_of_match']
    top_winner_location = season_query.filter(winner=top_four_teams[0]).values(
                'city').annotate(the_count=Count('city')).order_by('-the_count')[0]['city']
    max_hosted_location = season_query.exclude(city="").values(
                'city').annotate(the_count=Count('city')).order_by('-the_count')[0]['city']
    max_margin_of_runs_winner = season_query.values(
                'winner').annotate(win_by_runs_max=Max('win_by_runs')).order_by(
                "-win_by_runs_max")[0]['winner']
    max_number_of_wickets_winner = season_query.values(
                'winner').annotate(win_by_wickets_max=Max('win_by_wickets')).order_by(
                "-win_by_wickets_max")[0]['winner']
    toss_and_match_winner = ["{0} - {1}".format(i['winner'],i['winner_count']) for i in season_query.filter(
                toss_winner=F('winner')).values('winner').annotate(winner_count=Count(
                'winner')).order_by("-winner_count")]

    data.append({"title": "Top four teams",
                "value": top_four_teams, 
                'graph_url': redirect('match_win_details', season=season).url})
    data.append({"title": "Max toss winning team",
                "value": max_toss_winning_team, 
                'graph_url': redirect('toss_win_details', season=season).url})
    data.append({"title": "Max match winner",
                "value": top_four_teams[0], 
                'graph_url': redirect('match_win_details', season=season).url})
    data.append({"title": "Max player of match winner",
                "value": max_player_of_match_winner, 
                'graph_url': redirect('player_of_match_details', season=season).url})
    data.append({"title": "Top winner location",
                 "value": top_winner_location, 
                 'graph_url': None})
    data.append({"title": "Max hosted location",
                "value": max_hosted_location, 
                'graph_url': redirect('hosted_location_details', season=season).url})
    data.append({"title": "Max margin of runs Winner",
                "value": max_margin_of_runs_winner, 
                'graph_url': redirect('win_by_run_details', season=season).url})
    data.append({"title": "Max number of wickets winner",
                "value": max_number_of_wickets_winner, 
                'graph_url': redirect('win_by_wicket_details', season=season).url})
    data.append({"title": "Top four toss and match winner",
                "value": toss_and_match_winner[:4], 
                'graph_url': redirect('toss_and_match_winner_details', season=season).url})

    return render(request, template_name, {"seasons": seasons, 'data':data})


def highchart_column_data(query_result, key_string, value_string):
    res = []
    for i in query_result:
        res.append([i[key_string], i[value_string]])
    
    return res

def get_match_win_details(request, season):
    q = Match.objects.filter(
        season=season).values(
            'winner').annotate(the_count=Count('winner')).order_by('-the_count')
    response = {
        "title": 'IPL-{0} Matches'.format(season),
        "y-axis-title": "matches",
        "pointer-text": "Matches win in {0}:".format(season),
        "data-name": "Matches",
        "data": highchart_column_data(q,'winner','the_count')
    }

    return JsonResponse(response)

def get_toss_win_details(request, season):
    q = Match.objects.filter(
        season=season).values(
            'toss_winner').annotate(the_count=Count('toss_winner')).order_by('-the_count')
    response = {
        "title": 'IPL-{0} Toss wins'.format(season),
        "y-axis-title": "matches",
        "pointer-text": "Toss win in {0}:".format(season),
        "data-name": "Matches",
        "data": highchart_column_data(q,'toss_winner','the_count')
    }

    return JsonResponse(response)

def get_player_of_match_details(request, season):
    q = Match.objects.filter(season=season).values('player_of_match').annotate(the_count=Count('player_of_match')).order_by('-the_count')
    response = {
        "title": 'IPL-{0} Player of match'.format(season),
        "y-axis-title": "matches",
        "pointer-text": "Player of match {0}:".format(season),
        "data-name": "Matches",
        "data": highchart_column_data(q,'player_of_match','the_count')
    }

    return JsonResponse(response)

def get_hosted_location_details(request, season):
    q = Match.objects.filter(
        season=season).exclude(city="").values(
            'city').annotate(the_count=Count('city')).order_by('-the_count')
    response = {
        "title": 'IPL-{0} Matches hosted locations'.format(season),
        "y-axis-title": "matches",
        "pointer-text": "Location of match {0}:".format(season),
        "data-name": "Matches",
        "data": highchart_column_data(q,'city','the_count')
    }

    return JsonResponse(response)

def get_win_by_run_details(request, season):
    q = Match.objects.filter(
        season=season).values(
            'winner').annotate(the_count=Max('win_by_runs')).order_by('-the_count')
    response = {
        "title": 'IPL-{0} Match win by run'.format(season),
        "y-axis-title": "Runs",
        "pointer-text": "Runs of match {0}:".format(season),
        "data-name": "Runs",
        "data": highchart_column_data(q,'winner','the_count')
    }

    return JsonResponse(response)

def get_win_by_wicket_details(request, season):
    q = Match.objects.filter(
        season=season).values(
            'winner').annotate(the_count=Max('win_by_wickets')).order_by('-the_count')
    response = {
        "title": 'IPL-{0} Match win by wicket'.format(season),
        "y-axis-title": "Wickets",
        "pointer-text": "wickets of match {0}:".format(season),
        "data-name": "Wickets",
        "data": highchart_column_data(q,'winner','the_count')
    }

    return JsonResponse(response)

def get_toss_and_match_winner_details(request, season):
    q = Match.objects.filter(
        season=season,toss_winner=F('winner')).values(
            'winner').annotate(the_count=Count('winner')).order_by('-the_count')
    response = {
        "title": 'IPL-{0} Toss and match winner'.format(season),
        "y-axis-title": "Matches",
        "pointer-text": "match {0}:".format(season),
        "data-name": "Matches",
        "data": highchart_column_data(q,'winner','the_count')
    }

    return JsonResponse(response)

