import pandas as pd
import os
# get the names of all the files in input
files = os.listdir('input')

for name in files:

    data = pd.read_csv('input/' + name)
    data.drop('web-scraper-order', axis=1, inplace=True)
    data.drop('web-scraper-start-url', axis=1, inplace=True)

    data.to_csv('output/' + name, index=False)