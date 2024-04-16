import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import random
def get_photo_urls():
    photo_urls = []
    url = "https://gocsgo.net/guides/advice/avatarki-dlya-doty/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        for img in images:
            img_url = img.get('src')
            if img_url:
                img_url = urljoin("https://gocsgo.net/guides/advice/avatarki-dlya-doty/", img_url)
                photo_urls.append(img_url)
    
    return photo_urls
get_photo_urls()

folder_path = os.path.join('study/', 'downfile')
def files_func(photo_url):

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    img_inf = requests.get(photo_url).content
    print(f"Папка 'downfile' успішно створена.")
    rand = {random.randint(1, 1000000)}
    with open(os.path.join(folder_path, f'{rand}.jpg'), 'wb') as new_file:
        new_file.write(img_inf)

