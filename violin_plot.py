import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime

# Set the style of the grid and data
sns.set(style="whitegrid", color_codes=True)
np.random.seed(sum(map(ord, "categorical")))

# Upload the data
airbnb = pd.read_csv("sample.csv")

# Replace the column name with the new one
airbnb.columns = airbnb.columns.str.replace('country_destination;;;;','country_destination')

# Get weekday from date_account_created category
airbnb.date_account_created = airbnb.date_account_created.apply(lambda d: (datetime.strptime(d, "%m/%d/%Y")).year)

# Filter the age category
airbnbClean = airbnb[airbnb.age <= 80]

# Replace the names of selected countries with more appropriate ones
name = airbnbClean.replace({'country_destination' : { 'ES;;;;' : "Spain", 'US;;;;' : "US", 'FR;;;;' : "France", "IT;;;;": "Italy", "GB;;;;": "UK"}})

# Select specific countries from the data
g = name[(name.country_destination == "Spain") | (name.country_destination == "US") | (name.country_destination == "France") | (name.country_destination == "Italy") | (name.country_destination == "UK")]

# Select specific years from the data
k = g[(g.date_account_created != 2010)]

# Select specific gender type (getting rid of Nan and other values)
m = k[(k.gender == "FEMALE") | (k.gender == "MALE")]

# Create a map of the violin plots
p = sns.FacetGrid(m, col="date_account_created", size=4, aspect=.7, col_wrap=2, hue_order=["FEMALE", "MALE"], )
p = (p.map(sns.violinplot, "country_destination", "age", "gender", split=True, palette="RdBu", linewidth=1)).set_titles("{col_name}").set(ylim=(0,100)).add_legend().set_xlabels("Country destination").set_ylabels("Age")

sns.plt.show()

