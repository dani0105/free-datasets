import requests
from bs4 import BeautifulSoup
import pandas as pb
import os


# data source
TARGET = "https://datosmacro.expansion.com/energia-y-medio-ambiente/emisiones-co2/china"
#execution folder
CURRENT_FOLDER = os.getcwd()

#request html page
response = requests.post(url = TARGET)

# Convert html response to soap format for easy handling
soup = BeautifulSoup(response.content)

table = soup.find("table", { "id": "tb0" })

rows = table.find("tbody").find_all("tr")

data = []

for row in rows:
  record = []
  for cell in row.find_all("td"):
    value = cell.text
    #jump if the value is empty
    if value == '':
      record.append(None)
      continue

    #fix float format
    value=value.replace(".", "")
    value=value.replace(",", ".")
    content = float(value)

    record.append(content)
  data.append(record)

# create datafrem from data
frame =pb.DataFrame(data,
                    columns=["year", "co2_total_megatonne", "co2_kilogram_for_one_thousand_dollars", "co2_per_capita"])

# store resulting datafram in csv
frame.to_csv(os.path.join(CURRENT_FOLDER, "datasets", "CO2-emissions", "CN_CHINA.csv"),  index=False)

