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

def notice(request):
    #https://newweb.nepalstock.com.np/api/web/notice/
    if(request.method == "GET"):
        header = Headers(headers=True)
        result = requests.get("https://newweb.nepalstock.com.np/api/web/notice/",headers=header.generate())
        return JsonResponse({'marketStatus':result.json()})

def disclosure(request):
    #https://newweb.nepalstock.com.np/api/nots/news/companies/disclosure
    if(request.method == "GET"):
        header = Headers(headers=True)
        result = requests.get("https://newweb.nepalstock.com.np/api/nots/news/companies/disclosure",headers=header.generate())
        return JsonResponse({'marketStatus':result.json()})

def nepseIndex(request):
    #https://newweb.nepalstock.com.np/api/nots/nepse-index
    if(request.method == "GET"):
        header = Headers(headers=True)
        result = requests.get("https://newweb.nepalstock.com.np/api/nots/nepse-index",headers=header.generate())
        return JsonResponse({'marketStatus':result.json()})

def marketSummary(request):
    #https://newweb.nepalstock.com.np/api/nots/market-summary/
    if(request.method == "GET"):
        header = Headers(headers=True)
        result = requests.get("https://newweb.nepalstock.com.np/api/nots/market-summary/",headers=header.generate())
        return JsonResponse({'marketStatus':result.json()})

def topGainers(request):
    #https://newweb.nepalstock.com.np/api/nots/top-ten/top-gainer?all=false
    if(request.method == "GET"):
        header = Headers(headers=True)
        result = requests.get("https://newweb.nepalstock.com.np/api/nots/top-ten/top-gainer?all=false",headers=header.generate())
        return JsonResponse({'marketStatus':result.json()})

def topTurnovers(request):
    #https://newweb.nepalstock.com.np/api/nots/top-ten/turnover?all=false
    if(request.method == "GET"):
        header = Headers(headers=True)
        result = requests.get("https://newweb.nepalstock.com.np/api/nots/top-ten/turnover?all=false",headers=header.generate())
        return JsonResponse({'marketStatus':result.json()})

def supplyDemand(request):
    #https://newweb.nepalstock.com.np/api/nots/nepse-data/supplydemand?all=false
    if(request.method == "GET"):
        header = Headers(headers=True)
        result = requests.get("https://newweb.nepalstock.com.np/api/nots/nepse-data/supplydemand?all=false",headers=header.generate())
        return JsonResponse({'marketStatus':result.json()})
