from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)
soup = bs(page.text, 'html.parser')
table = soup.find_all('table')
temp_list = []
t_rows = table[7].find_all('tr')
for tr in t_rows:
    t_dta = tr.find_all('td')
    row = [i.text.rstrip() for i in t_dta]
    temp_list.append(row)
name = []
mass = []
radius = []
distance = []
for i in range(1, len(temp_list)):
    name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
df = pd.DataFrame(list(zip(name, distance, mass, radius)), columns = ['Star_Names', 'Star_Distance', 'Star_mass', 'Star_radius'])
df.to_csv('dwarfstars.csv')