from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Bets

import requests
from bs4 import BeautifulSoup
import lxml

import json
from django.core import serializers

# Create your views here.


def home_view(req, *args, **kwargs):
    # return HttpResponse("<h1>hello world</h1>")
    return render(req, "pages/home.html", context={}, status=200)


def bet_list_view(req, *args, **kwargs):
    """
    Rest Api view
    to be consumed by a client
    TODO make it using try catch like below 
    return JSON
    """
    qs = Bets.objects.all()

    qs = [{
        "bet_id": x.id,
        "home_points": x.home_points,
        "away_points": x.away_points,
        "match_id": x.match_id,
        "amount": x.amount, }
        for x in qs]
    data = {
        "isUser": False,
        "response": qs,
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
    data = []
    for i in range(len(titles)):
        data.append({
            "title": titles[i],
            "story": stories[i]
        })
    return JsonResponse(data, status=200, safe=False)
