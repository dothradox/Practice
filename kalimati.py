import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


a = requests.get("https://kalimatimarket.gov.np/")
soup = bs(a.text, "lxml")
table = soup.find_all("table")
raw_data = table[0].find_all("td")
data = [doc.get_text().split("रू") for doc in table[0].find_all("tr")]

df = pd.DataFrame.from_records(data)
df.columns = ["Name", "Min", "Max", "Average"]
print(df)