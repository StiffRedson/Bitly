import requests
import sys
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import argparse

load_dotenv()
secret_token = os.getenv("TOKEN")

if secret_token is None:
    print('[*]Sorry, something went wrong')
    sys.exit()

headers = {
    "Authorization": f"Bearer {secret_token}"
}


def shorten_link(my_url):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    response = requests.post(url, headers=headers, json=dict(long_url=my_url))
    response.raise_for_status()
    bitlink = response.json()
    return bitlink['link']


def count_clicks(clics):
    url_base = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    url_clicks = url_base.format(clics)
    response = requests.get(url_clicks, headers=headers, params=dict(units='-1', unit_reference=""))
    response.raise_for_status()
    clicks_all = response.json()
    return clicks_all['total_clicks']


def obtain_info(index):
    url_base = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
    url_info = url_base.format(index)
    response = requests.get(url_info, headers=headers)
    response.raise_for_status()
    info = response.json()
    return info


def create_parser():
    parser = argparse.ArgumentParser(description='Сокращает ссылку или считает кол-во переходов по короткой ссылке')
    parser.add_argument('-u', '--url', help='Сжать ссылку или расчитать клики')
    args = parser.parse_args(sys.argv[1:])
    return args.url


if __name__ == '__main__':

    my_url = create_parser()

    try:
        response = requests.get(my_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print("[*] Http Error:", http_err)
        exit(1)
    except requests.exceptions.ConnectionError as connect_err:
        print("[*] Error Connecting:", connect_err)
        exit(1)
    except requests.exceptions.RequestException as err:
        print('[*] Verify the link is correct \n', err)
        exit(1)

    try:
        split = urlparse(my_url)
        link_id = split[1] + split[2]
        reception = obtain_info(link_id)
        following_links = reception['id']
    except requests.exceptions.RequestException as err:
        print('[*] Your link is shortened\n')
        link = shorten_link(my_url)
        print("[*] Your shortened link:\n>>", link)
    else:
        print("\n[*] Number of clicks link:\n>>", count_clicks(following_links))
