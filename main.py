
import time
from time import sleep
import os
import time
from time import sleep
import requests
import pywebcopy
from pywebcopy import save_webpage
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError


storage_path=r'C:\Users\sareman\Desktop\Matt_tasks\webpages'

# SECOND I create empty web pages with numbers of web pages

def create_web_file(a, storage_path):
    file_name=f"\webpage{a}.html"
    path=(f"{storage_path}{file_name}")
    
    if os.path.exists(path):
        print('file already exists')
    else:
        with open(path, 'w') as fp:
            fp.write('0')

# THIRD I scape webpages into empty files which I have created earlier. 
#I have created session request to make mask to pass website cookies + add headers + delay 1 sec

def scrape_web_page(a, storage_path):
    file_name=f"\webpage{a}.html"
    path=(f"{storage_path}{file_name}")
    
    page_url=f'https://www.classcentral.com/university/stanford'
    end_page=f'?page='
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    
    with requests.Session() as s:
        sleep(2)
        url=f'{page_url}{end_page}{a}'
        r=s.get(url, headers=headers)
        open(path, 'wb').write(r.content)

        
 # FIRST I count pages, sometimes it is not possible due to huge volume pages and it is not possible to make it manually
 # So, here I could include some checks if the page exist (requests -200 exist, else not exist), or (check if some requesites exist on page by BS)

for page in range(0,52):
    sleep(1)
    a=page
    create_web_file(a, storage_path)
    scrape_web_page(a, storage_path)
    print(a)
    
    
  #FINALLY, I scraped main page as a main.html

main_page_url = f"https://www.classcentral.com/"
path_main_page= r'C:\Users\sareman\Desktop\Matt_tasks\webpages\main.html'

def scrape_main_page(main_page_url, path_main_page):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    
    with requests.Session() as s:
        sleep(2)
        r=s.get(main_page_url, headers=headers)
        open(path_main_page, 'wb').write(r.content)

scrape_main_page(main_page_url, path_main_page)

