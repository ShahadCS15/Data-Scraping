import requests
from requests import exceptions
from bs4 import BeautifulSoup
import pandas as pd


df = pd.read_excel(r'astro-revised.xlsx')

def create_soup(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        #print(soup)
        return soup
    except:
        return 'N/A'


def getSpec(soup):
    try:
        spec = soup.find('div', {'class': 'product attribute description'}).text.strip("\n").strip().split('\r\n')
        #print(spec)
        outer_dictionary= {}
        for i in spec:
            #print(i)
            lst = i.split(':')
            print(lst)
            inner_dictionary = {lst[0] : lst[1]}
            outer_dictionary.update(inner_dictionary)
        return outer_dictionary
    except:
        pass


df['soup'] = df['Identifier'].apply(lambda x:create_soup(x))
df = df.drop('Unnamed: 27', 1)
df['specifications'] = df['soup'].apply(lambda x:getSpec(x))
df_temp = df['specifications'].apply(pd.Series)
df_merged = pd.concat([df, df_temp], axis=1)
df_merged.to_excel('Astro_Output.xlsx')
