import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import lxml
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
url = "https://comic.naver.com/webtoon?tab=fri"

browser.get(url)
time.sleep(1)

soup = BeautifulSoup(browser.page_source, "lxml")

top3 = soup.find("ul", attrs = {"class" : "ContentList__content_list--q5KXY"})
title = top3.findAll("span", attrs = {"class" : "ContentTitle__title--e3qXt"})
author = top3.findAll("a", attrs = {"class" : "ContentAuthor__author--CTAAP"})
rate = top3.findAll("span", attrs = {"class" : "Rating__star_area--dFzsb"})

print("----------금요웹툰 20개----------")

# print(len(title), len(author), len(rate))
for i in range(len(title))[:20]:
    print(f"{i+1} - {title[i].text} || {author[i].text} || {rate[i].text}")
# for j in top3[:10]:
#     print(j.text)
