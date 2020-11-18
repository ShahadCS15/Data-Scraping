# Data-Scraping
This python project is intended to scrape technical specification of products from certain webpages and append them to an existing excel file. 

## Packages:
* BeautifulSoup + requests
* pandas + openpyxl
* csv

## Files Description:
* AstroSpec.py: This python file used to scrape specifications details from Astro webpages.
* AstroTest.xlsx: Excel file displays the newly appended scrapped data to already existing data.
* KnipexSpec.py: Python file for extracting technical-related data from Knipex webpages, that are structured in tabular HTML format.
* KnipexTest.csv: csv file contains the scraped data from the Knipex webpages.
* MergeExcel.py: Python code that is used to append the newly scrapped data with the original data in excel file.
