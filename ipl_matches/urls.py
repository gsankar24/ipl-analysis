"""ipl_matches URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from matches.views import (
    index,get_match_win_details,get_toss_win_details, get_player_of_match_details,
    get_hosted_location_details,get_win_by_run_details, get_win_by_wicket_details,get_toss_and_match_winner_details)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('match_win_details/<int:season>', get_match_win_details, name="match_win_details"),
    path('toss_win_details/<int:season>', get_toss_win_details, name="toss_win_details"),
    path('player_of_match_details/<int:season>', get_player_of_match_details, name="player_of_match_details"),
    path('hosted_location_details/<int:season>', get_hosted_location_details, name="hosted_location_details"),
    path('win_by_run_details/<int:season>', get_win_by_run_details, name="win_by_run_details"),
    path('win_by_wicket_details/<int:season>', get_win_by_wicket_details, name="win_by_wicket_details"),
    path('toss_and_match_winner_details/<int:season>', get_toss_and_match_winner_details, name="toss_and_match_winner_details"),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
