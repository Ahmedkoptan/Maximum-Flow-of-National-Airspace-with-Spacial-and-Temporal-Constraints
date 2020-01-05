This directory contains:

- GreedyFord.py
script that codes an Algorithm that combines Edmonds-Karp maximum flow algorithm with a Greedy earliest arrival flight selection approach to achieve optimal solution, which is the maximum capacity of the National Airspace from a source airport to a destination airport. This file reads the flight data from Allflights.csv

- aa_scape.py
script that scrapes American Airlines Flight Schedule website using Selenium and Beautiful Soup to collect flight information. This script stores the information in AAflights.csv

- delta_scrape.py
script that scrapes Delta Airlines Flight Schedule website using Selenium and Beautiful Soup to collect flight information. This script stores the information in Dlflights.csv

- united_scrape.py
script that scrapes United Airlines Flight Schedule website using Selenium and Beautiful Soup to collect flight information. This script stores the information in Unitedflights.csv

- merge.py
script that merges all 3 csv files from scraping process, along with capacity information from Capacities.csv file, into AllFlights.csv




This directory contains the scripts needed to scrape flight data 