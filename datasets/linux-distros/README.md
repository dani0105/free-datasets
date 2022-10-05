# Linux Distros

## Description
This dataset stores information on the ranking of the most popular Linux distros currently released.

## Format
The information is found in `LINUX_DISTROS.csv`, but you may want to delete this and run `distro_scraper.py` yourself to get more updated information. There are 4 columns in this dataset:
-  distro: The name of the distribution (ex. "Ubuntu")
-  start_date: The starting date of the data row.
-  end_date: The ending date of the data row.
-  score: The average number of hits per day (HPD) for this distro (ex. 3046, meaning 3046 people searched for this distro)
-  change: The direction of the score, i.e., whether it is growing in popularity or decreasing (ex. "level", meaning no change has occured; "up", meaning it is increasing, and "down", meaning is decreasing)

## Source
The information in this dataset was collected using the included web scraping script (`distro_scraper.py`), targeted toward [distrowatch.com](https://distrowatch.com/dwres.php?resource=popularity)

## Example
|distro     |start_date|end_date  |score|change|
|-----------|----------|----------|-----|------|
|SystemRescue|2022-09-05|2022-10-05|100  |level |
|Robolinux  |2022-09-05|2022-10-05|97   |level |
|NuTyX      |2022-09-05|2022-10-05|96   |down  |
|Elive      |2022-09-05|2022-10-05|91   |down  |
|Rescuezilla|2022-09-05|2022-10-05|90   |level |
|Live Raizo |2022-09-05|2022-10-05|87   |up    |
|Ubuntu Unity|2022-09-05|2022-10-05|85   |up    |
|Fatdog64   |2022-09-05|2022-10-05|75   |up    |
|Lakka      |2022-09-05|2022-10-05|74   |down  |
|XeroLinux  |2022-09-05|2022-10-05|72   |up    |
