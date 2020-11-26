import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from requests import exceptions
from bs4 import BeautifulSoup
import pandas as pd


def page_driver(item_category, item_id):
    try:
        driver = webdriver.Chrome('C:\\Users\\Shahad\\Downloads\\chromedriver_win32\\chromedriver.exe')
        driver.get('https://www.knipex.com/nc/en/home/')
        #driver.implicitly_wait(10)

        search_bar = driver.find_element_by_id('s')
        search_bar.send_keys(item_id)

        submit_button = driver.find_element_by_id('go')
        submit_button.click()

        group_item = driver.find_element_by_link_text(item_category)
        group_item.click()

        select_item = driver.find_element_by_link_text(item_id)
        select_item.click()

        url = driver.current_url
        return url
    except:
        pass


##
df = pd.read_excel(r'Knipex Dataset.xlsx')

def getURLs():
    url_lst=[]
    for i in df.index:
        url = page_driver(df['Sub-Category'][i], df['Identifier'][i])
        url_lst.append(url)
    return url_lst



urls = getURLs()
#print(urls)
df['webpage_to_be_scraped'] = urls

def create_soup(url):
    try:
        r = requests.get(url, verify=False)
        soup = BeautifulSoup(r.text, 'lxml')
        #print(soup)
        return soup
    except:
        return 'N/A'


def getSpec(soup):
    try:
        inner_dictionary = {}

        div = soup.find('div', {'id' : 'fragment-1'})
        body = div.contents[0].find_all('tr')
        for row in body:
            cols = row.findChildren(recursive=False)
            cols = [ele.text.strip() for ele in cols]
            cols.remove(cols[0])
            inner_dictionary.update({cols[0] : cols[1]})
        return inner_dictionary

    except:
        pass


df['soup'] = df['webpage_to_be_scraped'].apply(lambda x:create_soup(x))
df['specifications'] = df['soup'].apply(lambda x:getSpec(x))
df_temp = df['specifications'].apply(pd.Series)
df_merged = pd.concat([df, df_temp], axis=1)
df_merged.to_excel('Knipex_Output.xlsx')
