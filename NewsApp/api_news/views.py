from django.shortcuts import render
import requests
from django.http import HttpResponse
from datetime import datetime
from .models import History, get_account, Account
from .utils import get_formated_data, get_formated_url, get_news_categories
from django.template import RequestContext

# Create your views here.
def login_page(request):
    return render(request, 'login.html')

def login(request):
    email_address = request.POST['email_address']
    password = request.POST['password']
    try:
        user = Account.objects.get(email_address=email_address, password=password)
    except Exception as e:
        return HttpResponse("login failed")
    user_data = {
        "name" : user.firstname + " " + user.lastname,
        "id": user.id
    }
    return render(request, 'home.html', {"user_data": user_data})

def get_news(request):
    """
    This function will get all top headlines of india as country = in is passed in api.
    It will also fetch list of all recent search keywords of logged in user.

    #TODO: improve way of geting user id from request
    """
    user_id = request.GET.get("user_id", 1)
    base_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey='
    url = get_formated_url(base_url)
    try:
        response = requests.get(url).json()
    except Exception as e:
        return HttpResponse("Unable to call api")
    final_response = []
    search_history_list = []

    if response["status"] == "ok":
        final_response = get_formated_data(response)
        search_history = History.objects.filter(user_id=int(user_id)).order_by("id")[:10]
        search_history_list = [{"keyword": data.keyword, "id": data.id} for data in search_history]
        filter_categories = get_news_categories()
    else:
        return HttpResponse("Error in response")

    return render(request, 'home.html',  {"response": final_response, "history": search_history_list,
                                          "filters": filter_categories})

def search(request):
    """
    This function will perform query based of keyword entered by user.
    It will create entry in history table with base url and keyword.

    #TODO: improve way of geting user id from request
    """
    query = request.GET['search']
    user_id = request.GET.get('user_id', 1)
    base_url = f'https://newsapi.org/v2/everything?q={query}&apiKey='
    url = get_formated_url(base_url)
    try:
        response = requests.get(url).json()
    except Exception as e:
        return HttpResponse("Unable to call api")
    final_response = []
    if response["status"] == "ok":
        history_object, created = History.objects.get_or_create(keyword=query, url=base_url, user_id=user_id)
        final_response = get_formated_data(response)
    else:
        return HttpResponse("Error in response")
    return render(request, "search.html", {"response": final_response, "query": query})

def get_history(request):
    """
    This function will perform query based of keyword selected by user from recent search keyword list.

    #TODO: improve way of geting user id from request
    """
    query_id = request.GET['query_id']
    history_object = History.objects.get(id=int(query_id.strip(",")))
    url = history_object.url
    try:
        response = requests.get(url).json()
    except Exception as e:
        return HttpResponse("Unable to call api")
    final_response = []
    if response["status"] == "ok":
        final_response = get_formated_data(response)
    else:
        return HttpResponse("Error in response")
    return render(request, "search.html", {"response": final_response})
