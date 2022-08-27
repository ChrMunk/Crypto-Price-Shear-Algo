import datetime as dt
from distutils import text_file
from zipfile import ZipFile

import numpy as np

import pandas as pd

zf = ZipFile('cryptoprices.zip')

cols = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']


dfs = pd.concat({text_file.filename.split('.')[0]: pd.read_csv(zf.open(text_file.filename),
    usecols=cols)
    
    for text_file in zf.infolist()
    if text_file.filename.endswith('.csv')
    })

df = dfs.droplevel(1).reset_index().rename(columns={'index':'ticker'})

df = df.set_index(['Date', 'ticker'])

print(df)