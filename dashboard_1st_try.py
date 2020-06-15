# 
 
# dashboard_generator.py First Try
import operator
import os
import pandas
import datetime
 
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

sales = csv_data.to_dict("records")
total_sales = 0
for x in sales:
    total_sales = total_sales + x["sales price"]

def to_usd(my_price):
    return f"${my_price:,.2f}"
total_sales = to_usd(total_sales)

grouped = (csv_data.groupby(["product"])
    .agg({"sales price":sum})
    .sort_values(["sales price"],ascending=False))
    #.style.format('${0:,.2f}') #change to USD
    #.reset_index())

print("-----------------------")
print("MONTH: March 2018") #make dynamic

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: " + str(total_sales))
print("-----------------------")
print("TOP SELLING PRODUCTS:")

#print(str(grouped))
rank = 1
for d in grouped:
    print("  " + str(rank) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))
    rank = rank + 1

# print("  1) Button-Down Shirt: $6,960.35")
# print("  2) Super Soft Hoodie: $1,875.00")
# print("  3) etc.")

# SOURCE: https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do/9271479
# SOURCE: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory 
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