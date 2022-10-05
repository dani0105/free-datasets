"""
This module scrapes the distrowatch.com website for the top linux distros.
ORIGINAL REPO: https://github.com/dani0105/free-datasets
DATE: 2022-10-04
REQUIREMENTS: requests, bs4, pandas, re
"""


# IMPORTS

# Imports or providing the absolute date
import datetime
from dateutil.relativedelta import relativedelta

# Imports or handling the data
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup


# Define rs and bs4 objects
req = requests.get("https://distrowatch.com/dwres.php?resource=popularity", timeout=5)
soup = BeautifulSoup(req.content, "html.parser")

# Prevents repeating this twice
phr3 = soup.find_all("td", class_="phr3")

# Actual data
distro_names = [i.text for i in soup.find_all("td", class_="phr2")]
scores = [i.text for i in phr3]
change = [re.search(r"/a(.*?).png", i.findNext("img")["src"]).group(1) for i in phr3]

# Get absolute date for each set
twelve = (datetime.datetime.now() - relativedelta(months=12)).strftime("%Y-%m-%d")
six = (datetime.datetime.now() - relativedelta(months=6)).strftime("%Y-%m-%d")
three = (datetime.datetime.now() - relativedelta(months=3)).strftime("%Y-%m-%d")
one = (datetime.datetime.now() - relativedelta(months=1)).strftime("%Y-%m-%d")

# Create groups based on timeframe

twelve_mons = list(
    zip(
        distro_names[0:266],
        [twelve] * 266,
        [datetime.datetime.now().strftime("%Y-%m-%d")] * 266,
        scores[0:266],
        change[0:266],
    )
)
six_mons = list(
    zip(
        distro_names[266:532],
        [six] * 266,
        [datetime.datetime.now().strftime("%Y-%m-%d")] * 266,
        scores[266:532],
        change[266:532],
    )
)
three_mons = list(
    zip(
        distro_names[532:798],
        [three] * 266,
        [datetime.datetime.now().strftime("%Y-%m-%d")] * 266,
        scores[532:798],
        change[532:798],
    )
)
one_mon = list(
    zip(
        distro_names[798:1064],
        [one] * 266,
        [datetime.datetime.now().strftime("%Y-%m-%d")] * 266,
        scores[798:1064],
        change[798:1064],
    )
)

# Create dataframe from groups
df = pd.DataFrame(
    twelve_mons + six_mons + three_mons + one_mon,
    columns=["distro", "start_date", "end_date", "score", "change"],
)

# Save to csv (this will save in the same directory as where the script is run)

df.to_csv("LINUX_DISTROS.csv", encoding="utf-8", index=False)
