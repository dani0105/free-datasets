# Linux Distros

## Description
This dataset stores information on the ranking of the most popular Linux distros currently released.

## Format
The information is found in `LINUX_DISTROS.csv`, but you may want to delete this and run `distro_scraper.py` yourself to get more updated information. There are 4 columns in this dataset:
-  distro: The name of the distribution (ex. "Ubuntu")
-  timeframe: The period of time to which this row belongs to (ex. "12 mons", meaning this is the popularity ranking for the last 12 months)
-  score: The average number of hits per day (HPD) for this distro (ex. 3046, meaning 3046 people searched for this distro)
-  change: The direction of the score, i.e., whether it is growing in popularity or decreasing (ex. "level", meaning no change has occured; "up", meaning it is increasing, and "down", meaning is decreasing)

## Source
The information in this dataset was collected using the included web scraping script (`distro_scraper.py`), targeted toward [distrowatch.com](https://distrowatch.com/dwres.php?resource=popularity)

## Example
|distro     |timeframe|score|change|
|-----------|---------|-----|------|
|MX Linux   |12mons   |3046 |down  |
|EndeavourOS|12mons   |2761 |down  |
|Mint       |12mons   |2187 |down  |
|Manjaro    |12mons   |1725 |down  |
|Pop!_OS    |12mons   |1368 |down  |
|Ubuntu     |12mons   |1267 |down  |
|Fedora     |12mons   |1120 |down  |
|Debian     |12mons   |1100 |down  |
|Garuda     |12mons   |1023 |down  |
|Zorin      |12mons   |812  |down  |
