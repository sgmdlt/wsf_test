[![Python CI](https://github.com/sgmdlt/wsf_test/actions/workflows/main.yml/badge.svg)](https://github.com/sgmdlt/wsf_test/actions/workflows/main.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/133b6c9cc2b4369b3667/maintainability)](https://codeclimate.com/github/sgmdlt/wsf_test/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/133b6c9cc2b4369b3667/test_coverage)](https://codeclimate.com/github/sgmdlt/wsf_test/test_coverage)

## minobr scrapper

### simple cli tool for downloading photos from 'https://minobrnauki.gov.ru/about/deps/' 

----

## Installation


```bash
pip install --user git+https://github.com/sgmdlt/wsf_test
```

## Usage


```bash

$scraper -h

usage: scraper <table>

Download photos of employes from ministry of education site

positional arguments:
  table       table with names for renaming

options:
  -h, --help  show this help message and exit

$ scraper ./minobr_scrape_list.csv
```