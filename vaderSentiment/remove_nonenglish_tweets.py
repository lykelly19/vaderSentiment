import pandas as pd
import sys

df = pd.read_csv(sys.argv[1])
print(df.shape)
df = df.dropna(how = 'all')

# drop rows where tweet_lang != en
df.drop(df[df['tweet_lang'] != "en"].index, inplace = True)
print(df.shape)

df.to_csv(sys.argv[2])
