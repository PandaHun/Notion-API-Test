import requests
from pprint import pprint
from configure import token

url = 'https://api.notion.com/v1/pages/314d03479a6f4d22988b2553c0961a35/children?page_size=100'
version = '2021-05-13'
headers = {'Notion-Version': '2021-05-13', 'Authorization': 'Bearer ' + token}
if __name__ == '__main__':
    res = requests.get(url=url,
                       headers=headers)
    pprint(res.json())
