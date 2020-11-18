import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook


r = requests.get('http://www.astrotools.com/1-2-extra-heavy-duty-reversible-air-drill-500rpm.html')
soup = BeautifulSoup(r.text, 'html.parser')

#get the html text from <div>
specCont = soup.find('div', {'class': 'product attribute description'}).text.strip("\n").strip()

#store the html text in a list as a string
separated= str(specCont).splitlines()

#split the string based on the occurence of ':'
lst=[]
for i in separated:
    lst+= i.split(':')
#lst.remove(lst[0])

#convert the lst element into dictionary
dict = {lst[e]: lst[e + 1] for e in range(0, len(lst), 2)}

#load the excel file
filename = "test2ex.xlsx"
wb = load_workbook(filename)

#specify the dataframe
df = pd.DataFrame.from_dict(dict, orient = 'index')
df = df.transpose()

#append rows
for r in dataframe_to_rows(df, index=False, header=True):
    ws.append(r)
wb.save(filename)
