import pandas as pd

destinations = pd.read_csv("destinations.csv")
test = pd.read_csv("test.csv")

shape = test.shape

print shape

head = test.head(5)

print head


train["hotel_cluster"].value_counts()
