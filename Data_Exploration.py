import pandas as pd

# The most important part of the Pandas library is the DataFrame. A DataFrame
# holds the type of data you might think of as a table. This is similar to a 
# sheet in Excel, or a table in a SQL database.
df = pd.read_csv('melb_data.csv') # Read and Store the Data as Data Frame
print(df.describe()) # Printing Summary of Data Frame

# The results show 8 numbers for each column in your original dataset. 
# The first number, the count, shows how many rows have non-missing values.

# The second value is the mean, which is the average. Under that, std is
# the standard deviation, which measures how numerically spread out the values are.
