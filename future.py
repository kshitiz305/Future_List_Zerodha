import importlib
import subprocess

# List of package names to check and install
packages_to_check = ['requests', 'pandas']

for package in packages_to_check:
    try:
        importlib.import_module(package)
        print(f"{package} is installed.")
    except ImportError:
        print(f"{package} is not installed. Installing...")
        subprocess.check_call(['pip', 'install', package])
        print(f"{package} has been installed.")


import requests
from bs4 import BeautifulSoup
import pandas as pd

cookies = {
    '_cfuvid': 'jrpN8a3IqRfE4A3ALIquXSLKg_Cdm2UMxkfpXSdJPjI-1697354870445-0-604800000',
    '_pk_ref.2.1556': '%5B%22%22%2C%22%22%2C1697354871%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.2.1556': '807466cabd7b6df9.1697354871.',
    '_pk_ses.2.1556': '1',
    'ref': 'zerodha',
}

headers = {
    'authority': 'zerodha.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '_cfuvid=jrpN8a3IqRfE4A3ALIquXSLKg_Cdm2UMxkfpXSdJPjI-1697354870445-0-604800000; _pk_ref.2.1556=%5B%22%22%2C%22%22%2C1697354871%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.2.1556=807466cabd7b6df9.1697354871.; _pk_ses.2.1556=1; ref=zerodha',
    'referer': 'https://zerodha.com/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

response = requests.get('https://zerodha.com/margin-calculator/Futures/', cookies=cookies, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
rows = soup.find_all('tr')
headers = [header.text.strip() for header in rows[0].find_all('th')]
data = []
for row in rows[1:]:
    row_data = [cell.text.strip() for cell in row.find_all('td')]
    data.append(row_data)


def func(cell):
    if cell is not None:
        return pd.Series(cell.split('\n')[:2] if cell is not None else ['',''])
 
df = pd.DataFrame(data,columns= headers)
df.dropna(axis = 0,inplace=True)
df[["Contract","Date"]] = df["Contract"].apply(func)
df.to_csv('Final_Result.csv',index = False)
