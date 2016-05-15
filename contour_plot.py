import pandas as pd
import seaborn as sns
from datetime import datetime

# Set the style of the grid
sns.set(style="whitegrid", color_codes=True)

# Upload the data
airbnb = pd.read_csv("sample.csv")

# Get weekday from date_account_created category
airbnb.date_account_created = airbnb.date_account_created.apply(lambda d: (datetime.strptime(d, "%m/%d/%Y")).weekday())

# Filter the age category
airbnbClean = airbnb[airbnb.age <= 80]

# Create the contour plot with histograms on the axises
ax = sns.JointGrid(x="date_account_created", y="age", data=airbnbClean, ylim=(10,80), xlim=(0,6))
ax = ax.set_axis_labels(xlabel= "Weekday account created", ylabel="Age")
ax = ax.plot_joint(sns.kdeplot, cmap="Blues", shade=True)
ax = ax.plot_marginals(sns.distplot, kde=False, color="b")

sns.plt.show()