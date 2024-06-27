from bs4 import BeautifulSoup
import requests, sys
import urllib.parse
from gdown import download
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="URL of the page to download from")
parser.add_argument("auto_dl", help="Automatically download all files", default=False)
args = parser.parse_args()

response = requests.get(args.url)
soup = BeautifulSoup(response.text, 'html.parser')
# get all a tags with ext-link class
links = soup.find_all('a', class_='ext-link')
for link in links:
    actual_link = urllib.parse.unquote(link.get('href').split("?url=")[1])
    # ask user if they want to download the file
    print(f"Download {actual_link}? (Y/n)")
    if args.auto_dl or input().lower() == 'y':
        download(url=actual_link)
    continue