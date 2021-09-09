import requests
from bs4 import BeautifulSoup
from pypac import PACSession, get_pac
import os
from urllib.parse import urlparse

proxies = {'https': 'https://122.54.102.166:8888'}
with requests.session() as s:
    s.proxies.update(proxies)
    for i in range(1, 6):
        r = s.get('https://danbooru.donmai.us/posts?page=' + str(i) + '&tags=0930erina').text
        soup = BeautifulSoup(r, 'html.parser')
        for link in soup.find(id='posts-container').findAll('a', href=True):
            r2 = s.get('https://danbooru.donmai.us'+ link['href']).text
            soup2 = BeautifulSoup(r2, 'html.parser')
            link2 = soup2.find('img', id='image')['src']
            response = requests.get(link2)
            with open("eva_arts/" + os.path.basename(urlparse(link2).path), 'wb') as f:
                f.write(response.content)
