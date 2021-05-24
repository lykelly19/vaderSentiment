import pandas as pd
import sys

df = pd.read_csv(sys.argv[1])
print(df.shape)
df.dropna(subset=['latitude', 'longitude'], inplace=True)
df = df[(df.latitude != 0) & (df.longitude != 0)]
print(df.shape)
df.to_csv(sys.argv[2])
