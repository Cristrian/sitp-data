# The present script is to verify that all the csv files in the csv_data folder are valid

# We are going to use the polars module
import polars as pl

from pathlib import Path

df = pl.read_csv('csv_data/20240801.csv')

print(df.describe())