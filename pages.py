from pprint import pprint

import requests
from urllib.parse import urlencode

APP_ID = "367b11a6f4db4864a11b92547b83e3a7"
AUTH_URL = "https://oauth.yandex.ru/authorize"

auth_url_data = {
    "response_type": "token",
    "client_id": APP_ID
}

#print("?".join((AUTH_URL, urlencode (auth_url_data))))

TOKEN = "AQAAAAAZLTA6AATOPxu91MkYOkFBoh9mRmPZbZ4"


class YandexMetrikaUses:
    def __init__(self,token):
        self.token = token

    def get_counter_list(self):
        headers = {
            "Authorization": "OAuth {}".format(self.token),
            "Content-Type": "application/json"
        }
        response = requests.get("https://api-metrika.yandex.ru/management/v1/counters", headers=headers,
                                params={"pretty": 1})
        return response.json()


artyom = YandexMetrikaUses(TOKEN)

counters = artyom.get_counter_list()
pprint(counters)

def get_counter_visits(counter_id, token):
    headers = {
        "Authorization": "OAuth {}".format(token),
        "Content-Type": "application/json"
    }
    params = {
        "id": counter_id,
        "metrics": "ym:s:visits"
    }
    response = requests.get("https://api-metrika.yandex.ru/stat/v1/data", headers=headers,
                                params={"pretty": 1})
    return response.json()

visits = get_counter_visits("47650009", TOKEN)
pprint(visits)

def get_counter_users(counter_id, token):
    headers = {
        "Authorization": "OAuth {}".format(token),
        "Content-Type": "application/json"
    }
    params={
        "id": counter_id,
        "metrics": "ym:s:users"
    }
    response = requests.get("https://api-metrika.yandex.ru/stat/v1/data", headers=headers,
                                params={"pretty": 1})
    return response.json()

users=get_counter_users("47650009", TOKEN)
pprint(users)

def get_counter_pageviews(counter_id, token):
    headers = {
        "Authorization": "OAuth {}".format(token),
        "Content-Type": "application/json"
    }
    params = {
        "id": counter_id,
        "metrics": "ym:s:pageviews"
    }
    response = requests.get("https://api-metrika.yandex.ru/stat/v1/data", headers=headers,
                                params={"pretty": 1})
    return response.json()

pageviews = get_counter_pageviews("47650009", TOKEN)
pprint(pageviews)


