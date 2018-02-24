# SofaScoreScraper
Python scraping scripts to retrieve LaLiga player and match statistics

### Prerequisites

You can find a Python (3.5.2) virtual environment ready to go in the env_spotahome folder containing all of the required packages

You can find a list of all required packackes in requirements.txt

```
beautifulsoup4==4.6.0
certifi==2018.1.18
chardet==3.0.4
idna==2.6
lxml==4.1.1
pytz==2018.3
requests==2.18.4
```

### Getting all LaLiga player information

In order to obtain a CSV containing all basic data of LaLiga players run:

```
python player_scraper.py
```

This will save all the data in a file called players.csv in the current directory

This script also downloads each player's photo (if available) into a directory called /players

### Getting individual player statistics from LaLiga matches

In order to obtain the individual player statistics from one or more LaLiga matches, you must provide the match_stats_scraper.py script with a list of links to the corresponding webpages in SofaScore.

Go to line 444 and enter the desired links into the 'links' list.

Run:

```
python match_stats_scraper.py
```

This will save all the data in a file called totalStats.csv in the current directory

## Built With

* [Python](https://www.python.org/downloads/release/python-352/)
* [Pandas](https://pandas.pydata.org)
* [Numpy](http://www.numpy.org)
* [Selenium](https://selenium-python.readthedocs.io)

## Authors

* **Javier Urbistondo** - *Initial work* - [PurpleBooth](https://github.com/Urbistondo)
