# Script to download files from a link

import requests
import os
from datetime import datetime, timedelta

def download_file(url, file_path):
    if not os.path.exists(file_path):
        response = requests.get(url)
        with open(file_path, 'wb') as file:
            file.write(response.content)
            
            
if __name__ == '__main__':
    # ask for two dates  in terminal input in format YYYYMMDD
    # example: python download_data.py 20250205 20250206
    date_start = input('Enter start date in format YYYYMMDD: ')
    date_end = input('Enter end date in format YYYYMMDD: ')
    
    # convert do dates
    date_start = datetime.strptime(date_start, '%Y%m%d')
    date_end = datetime.strptime(date_end, '%Y%m%d')
    
    # calculate the number of days between the two dates
    num_days = (date_end - date_start).days + 1
    
    # download the files
    for i in range(num_days):
        date = date_start + timedelta(days=i)
        date_str = date.strftime('%Y%m%d')
        print(f'Downloading data for {date_str}')
        print(f'number {i + 1} of a total of {num_days}')
        
        # download the files
        download_file(url=f'https://storage.googleapis.com/validaciones_tmsa/ValidacionZonal/validacionZonal{date_str}.zip', 
                      file_path=f'data/{date_str}.zip')
