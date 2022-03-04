from unicodedata import category
from django.shortcuts import render
import requests
API_KEY = 'ce731c78861e41e7b04bb469c102768e'
# Create your views here.
def home(request):
    country = request.GET.get('country')
    category=request.GET.get('category')
    if country:
        url= f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data=response.json()
        articles = data['articles']
    else:
        url= f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data=response.json()
        articles = data['articles']



    context={
        'articles' : articles
    }
    return render(request, 'news_api/home.html', context)