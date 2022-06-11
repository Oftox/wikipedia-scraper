# wikipedia-scraper
Wikipedia scraper implemented in python with TUI and support for multiple languages.
It uses the "requests" library for scraping the HTML of wikipedia.org, and "BeautifulSoup4" for parsing the HTML.

## Usage
wikipedia-scraper takes in one parameter, it is the language abbreviation used by wikipedia. At the moment the supported abbreviations are: 'en' for English, 'ja' for Japanese, 'ru' for Russian and 'fi' for Finnish. An example using 'en': `python3 main.py en`

## Notice
Files "languages.txt" and "translations.txt" are supposed to be read by the program, and thereby not intended to be read or tampered with by users.
