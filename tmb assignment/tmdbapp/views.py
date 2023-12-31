from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.http import JsonResponse
from django.conf import settings
# Create your views here.
@csrf_exempt
def search_movie_name(request):
    try:
        if request.method != "GET":
            raise Exception ("method not allowed")
        else:
            api_key = settings.API_KEY
            url = f"https://api.themoviedb.org/3/discover/movie?page=1&include_video=false&include_adult=false&sort_by=popularity.desc&language=en-US&api_key={api_key}"
            response1 = requests.get(url).json()
            response1["results"] = sorted(response1["results"], key=lambda x: x['popularity'], reverse=True)
            response = JsonResponse(response1)
            return response
    except Exception as ex:
        return JsonResponse({
            "status" : "Failed",
            "message" : str(ex)
        })