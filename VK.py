import requests
from bs4 import BeautifulSoup
import random
import string
from urllib3.request import urlencode


headers = {
    'authority': 'www.kith.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}
#
# response = requests.get("https://vk.com/kontorabrd", headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')
# posts = str(soup.find_all('div', class_="page_block"))
# event = posts.find('div', class_="group_name").text.strip()
# print(event)
# # a class="line_cell"

session = requests.Session()
session.headers = {"User-Agent": "VKAndroidApp/4.13.1-1206 (Android 4.4.3; SDK 19; armeabi; ; ru)",
                   "Accept": "image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, */*"}

app_data = {
    'login': 79018320701,
    'password': 'SpotiFindUser'
}

params = {
    'grant_type': 'password',
    'scope': 'market',
    'client_id': 2274003,
    'client_secret': 'hHbZxrka2uZ6jB1inYsH',
    'validate_token': 'true',
    'username': app_data['login'],
    'password': app_data['password'],
    'v': 5.95,
    'device_id': "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
}


def get_access_token():
    answer = requests.get("https://oauth.vk.com/token", params=params).json()
    if "error" not in answer:
        pass
    else:
        raise PermissionError("invalid login|password!")
    # self.secret = answer["secret"]
    token = answer["access_token"]
    return token


def get_token():
    OAUTH_API_BASE_URL = 'https://oauth.vk.com/authorize'
    REDIRECT_URL = 'https://oauth.vk.com/blank.html'
    OAUTH_PARAMS = {
        'client_id': 51572549,
        'redirect_uri': REDIRECT_URL,
        'display': 'popup',
        'scope': 'docs',
        'response_type': 'token',
        'state': 'krasava'
    }
    print('Пожалуйста, перейдите по ссылке, скопируйте URL открывшейся страницы и введите его.')
    print('?'.join([OAUTH_API_BASE_URL, urlencode(OAUTH_PARAMS)]))
    URL = input()
    vk_token = URL.split('&')[0].split('=')[-1]
    return vk_token


def get_description():
    access_token = 'caf032f6caf032f6caf032f6c8c9e2ddb3ccaf0caf032f6aef44db1b72ebd57d175fada'
    url = (
        "https://api.vk.com/method/groups.getById?v={v}&group_id={group_id}&access_token={token}&fields={fields}".format(
            v=5.95,
            group_id="kontorabrd",
            token=access_token,
            fields='description'))
    answer = requests.get(url, params=params).json()['response'][0]['description']
    return answer


def get_catalog_info():
    token = get_token()
    url = (
        "https://api.vk.com/method/docs.get?v={v}&access_token={token}&owner_id={owner_id}".format(
            v=5.131,
            token=token,
            owner_id=-202406))
    answer = requests.get(url).json()
    return answer


print(get_catalog_info())
# 202406
