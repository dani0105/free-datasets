"""
This module scrapes the distrowatch.com website for the top linux distros.
ORIGINAL REPO: https://github.com/dani0105/free-datasets
DATE: 2022-10-04
REQUIREMENTS: requests, bs4, pandas, re
"""


# Imports
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

# Create groups based on timeframe

twelve_mons = list(
    zip(distro_names[0:266], ["12mons"] * 266, scores[0:266], change[0:266])
)
six_mons = list(
    zip(distro_names[266:532], ["6mons"] * 266, scores[266:532], change[266:532])
)
three_mons = list(
    zip(distro_names[532:798], ["3mons"] * 266, scores[532:798], change[532:798])
)
one_mon = list(
    zip(distro_names[798:1064], ["1mons"] * 266, scores[798:1064], change[798:1064])
)

# Create dataframe from groups
df = pd.DataFrame(
    twelve_mons + six_mons + three_mons + one_mon,
    columns=["distro", "timeframe", "score", "change"],
)

# Save to csv (this will save in the same directory as the script)
df.to_csv("LINUX_DISTROS.csv", encoding='utf-8', index=False)
