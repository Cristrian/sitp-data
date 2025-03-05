import zipfile
from pathlib import Path

# First we load all the list of zip files in the data folder

list_of_files = [f.name for f in Path('data').glob('*.zip')]
print(list_of_files)

# Now we unzip all the files in the csv_data folder
# We will use the zipfile module
for i, file in enumerate(list_of_files):
    print(f'Unzipping {file}. This is file number {i + 1} of {len(list_of_files)}')
    with zipfile.ZipFile(f'data/{file}', 'r') as zip_ref:
        zip_ref.extractall(f'csv_data/')