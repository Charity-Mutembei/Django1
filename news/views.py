from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Articles
#Create views here
def welcome(request):
    return render(request, 'welcome.html')


def past_days_news(request, past_date):
    #converts data from the string urls
    try:
        #converts data from the string url
        date = dt.datatime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        #raise 404 error when ValueError is thrown
        raise Http404()
        assert False

        if date == dt.date.today():
            return redirect(news_today)


        news = Articles.days_news(date)

        return render(request, 'all-news/past-news.html', {"date": date})

def news_of_day(request):
    date = dt.date.today()

    return render(request, 'all-news/today-news.html', {"date": date,})
def news_today(request):
    date = dt.date.today()
    news = Articles.today_news()
    return render(request, 'all-news/today_news.html', {'date': date, 'news':news})
def search_results(request):
    if 'article' in request.GET and request.GET['article']:
        search_term = request.GET.get('article')
        searched_articles = Articles.search_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'all-news/search.html', {'message': message, 'articles': searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html', {'message': message})