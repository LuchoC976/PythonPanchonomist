# Pandas example
import pandas as pd
import numpy as np

# Construct a dataframe from a dictionary
data = {
    "col1": [1,2,3],
    "col2": [5,3,2]
}

dataframe = pd.DataFrame(data)
print("Dictionary frame: ")
print(dataframe)

# Using numpy arrays
data2 = np.array([(1,2,3), (4,5,6)])

df2 = pd.DataFrame(data2)
print("Numpy array: ")
print(df2)

# Open .csv files
datafile = pd.read_csv("~/consumers-price-index-June-2021-quarter-index-numbers.csv")

print("CSV File head: ")
print(datafile.head()) 
