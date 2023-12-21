#This example demonstrates how to read data from a file into a pandas DataFrame.
import numpy as np
import pandas as pd

#Read data from the file called 'credit.csv' into a DataFrame
article_read = pd.read_csv('credit.csv',
                            delim_whitespace = 1)#specify tha the delimiter is a single space

print(article_read)#Prints the entire file that was read
print(article_read.sample(5))#prints the number of rows specified 
print(article_read.head())#prints the first 5 rows
print(article_read.tail())#prints the last 5 rows
