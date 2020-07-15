from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Bets, User


import requests
from bs4 import BeautifulSoup
import lxml

# Create your views here.


def home_view(req, *args, **kwargs):
    # return HttpResponse("<h1>hello world</h1>")
    return render(req, "pages/home.html", context={}, status=200)


def bet_list_view(req, *args, **kwargs):
    """
    Rest Api view
    to be consumed by a client
    TODO return all required data from bets here
    return JSON
    """
    qs = Bets.objects.all()
    bet_list = [{"home": x.home_points, "owner": x.owner} for x in qs]
    data = {
        "isUser": False,
        "response": bet_list
    }
    return JsonResponse(data)


def bet_detailed_view(req, bet_id, *args, **kwargs):
    """
    Rest Api view
    to be consumed by a client
    return JSON 
    """
    data = {
        "id": bet_id,
    }
    status = 200

    try:
        obj = Bets.objects.get(id=bet_id)
        data["home"] = obj.home_points
        data["away"] = obj.away_points
    except:
        data["message"] = "Not found"
        status = 404

    return JsonResponse(data, status=status)


def news_view(req, *args, **kwargs):
    source = requests.get('https://www.skysports.com/football/news').text
    soup = BeautifulSoup(source, 'lxml')

    news_list = soup.find_all('div', class_='news-list__body')

    titles = []
    stories = []
    for news in news_list:
        title = news.find('a', class_='news-list__headline-link').text.strip()
        titles.append(title)
        story = news.find('p', class_='news-list__snippet').text.strip()
        stories.append(story)

    for i in range(len(titles)):
        print(titles[i])
        print(stories[i])
        print(" ")

    data = {
        "titles": titles,
        "stories": stories
    }
    return JsonResponse(data, status=200)
