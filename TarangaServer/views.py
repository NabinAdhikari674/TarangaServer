import requests
from fake_headers import Headers
from django.http import JsonResponse

def stockInfo(request):
    if(request.method == "GET"):
        header = Headers(headers=True)
        result = requests.get("https://newweb.nepalstock.com.np/api/nots/securityDailyTradeStat/58",headers=header.generate())
        return JsonResponse({'stockInfo':result.json()})

def marketStatus(request):
    #https://newweb.nepalstock.com.np/api/nots/nepse-data/market-open
    if(request.method == "GET"):
        header = Headers(headers=True)
        result = requests.get("https://newweb.nepalstock.com.np/api/nots/nepse-data/market-open",headers=header.generate())
        return JsonResponse({'marketStatus':result.json()})
