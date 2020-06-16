# dashboard_generator.py

#SOURCE: https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales_alt.py

import operator
import os
import pandas
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

# SOURCE: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

data_csv_folder = os.path.join(os.path.dirname(__file__), "data")

from os import listdir
from os.path import isfile, join
datafiles = [f for f in listdir(data_csv_folder) if isfile(join(data_csv_folder, f))]

# SOURCE: https://stackoverflow.com/questions/12116348/if-statement-to-control-user-input

while True:
    file_select = input("Please enter desired Monthly Sales file: ")
    if [m for m in datafiles if m == file_select]:
         print("MONTHLY SALES DATA")
         break
    else:
         print("Sorry! File does not exist.")

csv_filepath = os.path.join(os.path.dirname(__file__), "data",str(file_select))

csv_data = pandas.read_csv(csv_filepath, delimiter=",")

# SOURCE: https://stackoverflow.com/questions/54053680/datetime-in-python-importing-csv

# csv_data["date"] = pandas.to_datetime(csv_data["date"])

#data = []
#for row in csv_data["date"]:
#    date = datetime.datetime.strptime("%Y-%m-%d")
# df["date"] = pd.to_datetime(df["date"])
# month_year_title = csv_data["date"]

print("-----------------------")
print("MONTH: " + "FIX THIS") #make date dynamic
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

#Pie Chart
# SOURCE: https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_and_donut_labels.html
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

products = []
sales = []

for h in top_sellers:
    products.append(h["name"])
    sales.append(h["monthly_sales"])

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%".format(pct, absolute)

wedges, texts, autotexts = ax.pie(sales, autopct=lambda pct: func(pct, sales),
                                  textprops=dict(color="w"))

ax.legend(wedges, products,
          title="Products",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Top Selling Products (Month_Year)", weight="bold")

plt.show()

#Bar Chart
# SOURCE: https://pythonspot.com/matplotlib-bar-chart/
# SOURCE: https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales_alt.py
# SOURCE: https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh
y = []
x = []

for p in top_sellers:
    y.append(p["name"])
    x.append(p["monthly_sales"])

y_pos = np.arange(len(y))

fig, ax = plt.subplots()
usd_formatter = ticker.FormatStrFormatter('$%1.0f')
ax.xaxis.set_major_formatter(usd_formatter)

for i, v in enumerate(x):
    ax.text(v + 3, i + .25, str(to_usd(v)), color='black')

ax.invert_yaxis()

plt.barh(y, x)
plt.title('Top Selling Products (Month_Year)') #FIX MONTH YEAR
plt.yticks(y_pos, y)
plt.ylabel('Product')
plt.xlabel('Monthly Sales (USD)')

plt.tight_layout()
plt.show()