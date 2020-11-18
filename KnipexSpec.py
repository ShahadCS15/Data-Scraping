import csv
import requests
from bs4 import BeautifulSoup


URL= 'https://www.knipex.com/index.php?id=1216&L=1&page=group_detail&parentID=1299&groupID=1305'
r = requests.get(URL, verify=False)
soup = BeautifulSoup(r.text, 'lxml')



file = open('KnipexTest.csv', 'w', newline= '')
writer = csv.writer(file)


#Both statements are used depending on the table structure on the webpage
tbody = soup('table', {'class' : 'cont'})[0].find_all('tr')
#tbody = soup('table', {'id' : 'my-table'})[0].find_all('tr')

for row in tbody:
    cols = row.findChildren(recursive=False)
    cols = [ele.text.strip() for ele in cols]
    writer.writerow(cols)
    print(cols)

file.close()
