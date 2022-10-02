import requests
from bs4 import BeautifulSoup
import json
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException




def get_data_from_search(driver, search, class_to_wait_for):

    driver.get(search)
    try:
        myElem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, class_to_wait_for)))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_links(soup):
    articles = soup.find_all('article', class_='hLxOCk')
    links = []
    for article in articles:
        # print(article.find('span', class_='krgAt'))
        link = article.find('a', class_='iqASGc')['href']
        links.append(link)
    return links

def load_posts(driver, links):
    posts = []
    for link in links:
        search = r'https://www.blocket.se' + link
        soup = get_data_from_search(driver, search, 'kIhjJa')
        try:
            title = soup.find('h1', class_='dGnKKn').text
            price = soup.find('div', class_='kIhjJa').text
            location = soup.find('a', class_='bEePwY').text
            description = soup.find('div', class_='gLpiBo').text
        except:
            print(search)
            title = ''
            price = ''
            location = ''
            description = ''

        post = {
            'title': title,
            'price': price,
            'location': location,
            'description': description,
            'link': search
        }
        posts.append(post)
        time.sleep(1)
    return posts

def write_to_json(json_name, posts):
    json_string = json.dumps(posts)
    with open(json_name, 'w') as json_file:
        json_file.write(json_string)
        json_file.close()




def scrape_data_to_json(searches, json_name):
    driver = webdriver.Safari()
    links = []
    for search in searches:
        search_soup = get_data_from_search(driver, search, 'krgAt')
        links.extend(get_links(search_soup))
    posts = load_posts(driver, links)
    write_to_json(json_name,posts)
