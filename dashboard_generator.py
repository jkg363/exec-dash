# dashboard_generator.py


#DISPLAYS ACCURATE INFO

# csv header: date, product, unit price, units sold, sales price

import operator
import os
import pandas
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

# CAPTURE FILES SELECTION 

# OPTION C: use the os module to detect the names of all CSV files which exist in the "data" directory, then display this list to the user and prompt the user to input their selection.

#FAILS GRACEFULLY IF FILE DOESN'T EXIST

# if incorrect option is selected, end script

csv_filename = "sales-201803.csv" # TODO: allow user to specify

csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

csv_data = pandas.read_csv(csv_filepath)

print("-----------------------")
print("MONTH: March 2018") #make date dynamic

print("-----------------------")
print("CRUNCHING THE DATA...")

monthly_total = csv_data["sales price"].sum()
monthly_total_usd = to_usd(monthly_total)

print("-----------------------")
print("TOTAL MONTHLY SALES: " + str(monthly_total_usd))

print("-----------------------")
print("TOP SELLING PRODUCTS:")

product_names = csv_data["product"]
unique_product_names = product_names.unique()
unique_product_names = unique_product_names.tolist()

top_sellers = []

for product_name in unique_product_names:
    matching_rows = csv_data[csv_data["product"] == product_name]
    product_monthly_sales = matching_rows["sales price"].sum()
    top_sellers.append({"name": product_name, "monthly_sales": product_monthly_sales})

top_sellers = sorted(top_sellers, key=operator.itemgetter("monthly_sales"), reverse=True)

rank = 1
for d in top_sellers:
    print("  " + str(rank) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))
    rank = rank + 1

print("-----------------------")
print("VISUALIZING THE DATA...")

#DISPLAYS CHARTS AND GRAPHS INCLUDING TITLES AND AXIS LABELS
#SOURCE: https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales_alt.py
