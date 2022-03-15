import pandas as pd
from pandas.io.json import json_normalize

# Reads the json generated from the CLI commands above and creates a pandas dataframe
tweets_df = pd.read_json('snscraptest.json', lines=True)
tweets_df.to_csv()
#print(tweets_df['coordinates']['latitude'])
