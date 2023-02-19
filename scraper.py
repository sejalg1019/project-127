from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

url= "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

request= requests.get(url)

soup = bs(request.text, "html.parser")
star_data = soup.find("table")
data = []

table_rows = star_data.find_all("tr")

for tr in table_rows:
    table_data= tr.find_all("td")
    row= [i.text.rstrip() for i in table_data]
    data.append(row)


name = []
distance = []
mass = []
radius = []

for i in range(1,len(data)):
    name.append(data[i][1])
    distance.append(data[i][3])
    mass.append(data[i][5])
    radius.append(data[i][6])


df = pd.DataFrame(list(zip(name, distance, mass, radius)),columns=["star_name", "star_distance", "star_mass", "star_radius"])
print(df)

df.to_csv("star_data.csv")
