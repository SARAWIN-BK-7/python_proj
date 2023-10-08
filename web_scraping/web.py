import pandas as pd 
import bs4 
import requests 
import openpyxl

page = 1
name_list = []
price_list = []
while page <= 10:
  data = requests.get('https://www.checkraka.com/car/?quicksearch_order=update%2CDESC&page=' + str(page))
  soup = bs4.BeautifulSoup(data.text)
  for c in soup.find_all('div',{'class':'content c158'}):
    name_list.append(c.find('div',{'class':'data'}).find('a').text)
    p = c.find('div',{'class':'price'}).text.split()[0].replace(',','')
    if p == 'call':
      price_list.append(p)
    else:
      price_list.append(int(p))
  print('Complete page number: ',page)
  page += 1
table = pd.DataFrame([name_list,price_list]).transpose()
table.columns = ['name','price']
table.set_index('name')
table.to_excel('All Cars.xlsx',engine='openpyxl')
        