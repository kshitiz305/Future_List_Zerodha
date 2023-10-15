# NSE Market Future Contract Scraper

This Python script allows you to scrape the futures contracts data from the National Stock Exchange (NSE) market. It uses web scraping to gather contract information and saves it to a CSV file for further analysis.

## Setup Instructions

To run this script, you need to install the required Python packages. You can do this by following these steps:

1. **Clone the Repository** (if not already done):

   ```shell
   git clone https://github.com/kshitiz305/Future_List_Zerodha.git
   cd Future_List_Zerodha

2. **Install Required Packages:**

Make sure you have Python installed on your system. To install the required packages, you can use the following command:

  ```shell
    pip install -r requirements.txt
  ```
  
This will install the necessary packages, which are requests, pandas, and beautifulsoup4.

3. **Run the Script:**

You can run the script using the following command:

```shell
python nse_futures_scraper.py

```

This will execute the script, which will scrape the data and save it to a file named Final_Result.csv.

## Script Explanation
The script does the following:

1. Checks if the required Python packages (requests, pandas) are installed. If not, it installs them automatically.

2. Sends an HTTP GET request to the Zerodha margin calculator page, which contains futures contract data.

3. Parses the HTML content of the page using BeautifulSoup.

4. Extracts the data from the HTML table.

5. Processes the data to clean and format it.

6. Saves the cleaned data to a CSV file named Final_Result.csv.

Please ensure you have the necessary permissions to scrape data from website. Additionally, make sure you comply with their terms and conditions while using this script.

For any questions or issues, please contact the script author or maintainers kshtiiz305@live.com .
