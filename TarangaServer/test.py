import requests
import pandas as pd
import os
import random
from fake_headers import Headers


path = os.path.join(os.getcwd(),"TarangaServer","Resources","user_agent.csv")
user_agents = pd.DataFrame(pd.read_csv(path))
def django_view():
    print("Sending Request...")
    header = Headers(headers=True)
    '''
    response = requests.get('https://newweb.nepalstock.com.np/api/nots/securityDailyTradeStat/58',
                            headers={
                            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                            "accept-encoding":"gzip, deflate, br",
                            #"content-type":"application/json",
                            "accept-language":"en-US,en;q=0.5",
                            "connection":"keep-alive",
                            "dnt":"1",
                            "host":"newweb.nepalstock.com.np",
                            #"te":"Trailers",
                            "upgrade-insecure-requests":"1",
                            "user-agent":user_agents["user_agent"][random.randint(0,9999)]})
    '''
    response = requests.get("https://newweb.nepalstock.com.np/api/nots/securityDailyTradeStat/58",headers=header.generate())
    print(response.status_code)
    #print(response.headers)
    #print(response.encoding)
    #print(response.text)
    #print(response.json())
django_view()
