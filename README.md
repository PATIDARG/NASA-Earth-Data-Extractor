# NASA-Earth-Data-Extractor
This repository contains a Python script that extracts data from NASA Earth Data's webpage haqast-overview. The script uses the requests library to fetch the webpage content and BeautifulSoup to parse the HTML.  The extracted data is then saved in a CSV file.
# Data Extraction from NASA Earth Data

This repository contains a Python script that extracts data from NASA Earth Data's webpage [haqast-overview](https://www.earthdata.nasa.gov/learn/articles/haqast-overview).
## Prerequisites

- Python 3.x
- Required libraries: `requests`, `beautifulsoup4`
## Installation

1. Clone this repository to your local machine:


2. Install the required libraries:

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
  ## Dependencies

- Python 3.x
- requests
- beautifulsoup4

## References

- [NASA Earth Data API documentation](https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api)
