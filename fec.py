import pandas as pd

data = pd.read_csv("data/oppexp.txt", sep="|", header=None)
print(data.head())