# wikipedia-scraper
It is a Wikipedia scraper implemented in python with text-based user interface and support for multiple languages.

It uses the "[requests](https://pypi.org/project/requests/)" library for scraping the HTML of wikipedia.org, and "[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)" for parsing the HTML.

## Usage
It can be used to search for wikipedia articles, and is basically a text-based Wikipedia client.
wikipedia-scraper takes in one parameter, the language abbreviation used by wikipedia in the URL. 

Currently the supported abbreviations include: 'en' for English, 'ja' for Japanese, 'ru' for Russian and 'fi' for Finnish. 

An example of usage: 
`python3 main.py en`

## Notice
Files "languages.txt" and "translations.txt" are supposed to be read by the program, and thereby not intended to be read or tampered with by users.
