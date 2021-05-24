import pandas as pd

df = pd.read_csv("geotweets(Mar - Feb).csv")

print(len(df))
df = df.dropna(subset=["tweet_lang"])
print(len(df))

df = df.apply(lambda x : True
            if x['tweet_lang'] == "en" else False, axis = 1)



# Count number of True in the series
num_rows = len(df[df == True].index)
print(num_rows)

num_rows = len(df[df == False].index)
print(num_rows)


# https://www.geeksforgeeks.org/count-all-rows-or-those-that-satisfy-some-condition-in-pandas-dataframe/
