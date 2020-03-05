import pandas as pd 
f_scrip = pd.read_csv('file')
# Columnns in this dataframe are 'symbol,open, high, low, close'

for index, row in f_scrip.iterrows():
  high = row('high')
  symbol,high = row['symbol'],row['high']



