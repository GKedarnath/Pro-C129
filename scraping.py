from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/list_of_brightest_stars_and_other_record_stars"

page = requests.get(start_url)

time.sleep(10)
soup = BeautifulSoup(page.text, "html.parser")
start_table = soup.find('table')

table_rows = start_table.find_all('tr')

temp_list = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1, len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])
    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)), columns = ['Star_names', 'Distance', 'Mass', 'Radius', 'Luminosity'])
df2.to_csv("bright_stars.csv")