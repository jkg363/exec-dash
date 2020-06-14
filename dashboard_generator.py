# dashboard_generator.py

import os
import datetime
import numpy as np
import pandas as pd

# csv_filepath = "data\sales-201803.csv"

csv_filepaths = []
while True:
    csv_filepath = input("Please input desired csv file: ")
    if csv_filepath == csv_filepaths.append(csv_filepath):
        break
    else:
    print(Hey, are you sure)
df = pd.read_csv(csv_filepath, delimiter = ',', skiprows = 0)



sales = df.to_dict("records")
total_sales = 0
for x in sales:
    total_sales = total_sales + x["sales price"]

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"
total_sales = to_usd(total_sales)

print("-----------------------")
print("MONTH: March 2018") #make dynamic

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: " + str(total_sales))
print("-----------------------")
print("TOP SELLING PRODUCTS:")

grouped = (df.groupby(["product"])
    .agg({"sales price":sum})
    .sort_values(["sales price"],ascending=False))
    #.style.format("${0:,.2f}") #change to USD
    #.reset_index())
print(str(grouped))

# print("  1) Button-Down Shirt: $6,960.35")
# print("  2) Super Soft Hoodie: $1,875.00")
# print("  3) etc.")

# SOURCE: https://stackoverflow.com/questions/27842613/pandas-groupby-sort-within-groups
# SOURCE: https://stackoverflow.com/questions/36073984/pandas-sorting-observations-within-groupby-groups
# SOURCE: https://stackoverflow.com/questions/51866908/difference-between-as-index-false-and-reset-index-in-pandas-groupby/51933722 


print("-----------------------")
print("VISUALIZING THE DATA...")


# import plotly
# import plotly.graph_objects as go
# 
# products = []
# products.append("product")
# 
# total_itemized_sales = []
# total_itemized_sales.append("total_sales")
# 
# fig = go.Figure(go.Bar(
#     x=[products],
#     y=[total_itemized_sales],
#     orientation='h'))
# 
# fig.show()
# 
# # SOURCE: https://plotly.com/python/horizontal-bar-charts/