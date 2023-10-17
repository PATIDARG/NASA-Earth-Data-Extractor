# NASA-Earth-Data-Extractor
This repository contains a Python script that extracts data from NASA Earth Data's webpage haqast-overview. The script uses the requests library to fetch the webpage content and BeautifulSoup to parse the HTML.  The extracted data is then saved in a CSV file with metadata including identifier, original ID 
# Data Extraction from NASA Earth Data

This repository contains a Python script that extracts data from NASA Earth Data's webpage [haqast-overview](https://www.earthdata.nasa.gov/learn/articles/haqast-overview).

- NASA-Earth-Data-Extractor
    - main.py
    - nasa_data.csv
    - README.md
    - LICENSE

## Prerequisites

- Python 3.x
- Required libraries: `requests`, `beautifulsoup4`
## Installation

Python:

Python is the primary programming language for this task. Make sure you have Python installed on your system. You can download it from the official website: Python Official Website.
Requests:

The requests library is used for making HTTP requests to retrieve data from websites. You can install it using pip:

pip install requests

Beautiful Soup (bs4):

Beautiful Soup is a Python library for web scraping purposes to pull the data out of HTML and XML files. You can install it using pip:

pip install beautifulsoup4

HTML Parser (lxml):

Lxml is a high-performance, production-quality XML and HTML parsing library. It is required by Beautiful Soup. Install it using pip:

pip install lxml

and  extracted data to a CSV file. It is a built-in Python library.


## Usage

1. Run the script:

The script will fetch the webpage, extract the data, and save it in a CSV file named `nasa_data.csv`.

## Data Fields

The extracted data contains the following fields:

- Identifier
- Original ID
- Sample Frequency
- Name
- Description
- ...

## References

- [NASA Earth Data API documentation](https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api)
