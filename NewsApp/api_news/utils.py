from django.conf import settings

def get_formated_data(response):
    """
    As response structure of all api's similar, calling this function 
    will get formated response for all apis.
    """
    final_response = []
    news_data = response["articles"]
    for data in news_data:
        if data["title"] != '[Removed]':
            final_response.append(
                {"title": data["title"], "author": data["author"], "description": data["description"],
                    "image": data["urlToImage"], "url": data["url"], "date": data["publishedAt"]}
            )
    final_response.sort(key = lambda x:x['date'], reverse=True)
    return final_response

def get_formated_url(url):
    """
    Adding api key
    """
    final_url = url + settings.APIKEY
    return final_url

def get_news_categories():
    categories = ["cricket", "singing", "politics", "india", "football"]
    return categories