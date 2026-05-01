import pandas as pd

a = [1,2,3]
b = [2,3,5]

d = {
    "Col1": a,
    "Col2": b
}

df = pd.DataFrame(d)

print(df)

df["Sum"] = df["Col1"] + df["Col2"]

print(df)