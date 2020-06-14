# dashboard_generator.py

import pandas
import os

csv_filepath = "data\sales-201803.csv"
df = pandas.read_csv(csv_filepath)
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
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: " + str(total_sales))
print("-----------------------")
print("TOP SELLING PRODUCTS:")
grouped = df.groupby(['product']).sum()
print(str(grouped))

# print("TOP SELLING PRODUCTS:")
# print("  1) Button-Down Shirt: $6,960.35")
# print("  2) Super Soft Hoodie: $1,875.00")
# print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")