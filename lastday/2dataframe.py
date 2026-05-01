import pandas as pd


d = {
    "col1" : [ 1,2,3 ],
    "col2" : ["A","B","C"]
}

df = pd.DataFrame(d)

df.dropna(inplace=True)
print(df)
df = df[df["col2"] != "A"]

print(df)