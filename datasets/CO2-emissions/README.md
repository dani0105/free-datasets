# CO2 Emissions

## Description
This dataset stores information on the CO2 emissions of the countries.

## Format
The information are store for country in `csv` files. I store the information in 4 columnas:
-  year: year of data record
-  co2_total_megatonne: Megatons of CO2 emitted
-  co2_kilogram_for_one_thousand_dollars: Kilograms of CO2 emissions per $1,000 of GDP
-  co2_per_capita: tons of CO2 emissions per capita

## Example
| year   | co2_total_megatonne | co2_kilogram_for_one_thousand_dollars | co2_per_capita |
| ------ | ------------------- | ------------------------------------- | -------------- |
| 2021.0 | 12466.316           | 0.5                                   | 8.73           |
| 2020.0 | 11948.12            | 0.52                                  | 8.39           |
| 2019.0 | 11771.073           | 0.52                                  | 8.29           |
| 2018.0 | 11499.292           | 0.54                                  | 8.13           |
| 2017.0 | 11036.735           | 0.55                                  | 7.83           |
| 2016.0 | 10794.286           | 0.58                                  | 7.69           |

## Contribution
I wrote a python script that can be used to get more information from other countries. Store the country information in different files and use the `Abreviation_Country.csv` format. To run python script you need to run `pip install -r requirements.txt`.