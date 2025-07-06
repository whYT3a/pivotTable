# Pivot table program to summarize dataset and offer Interactive visualisations of notable trends

# Import Packages 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import enum as enum
import sys

# Load and read in data in a dataframe
dataFilePath = input("Please enter your data file path here: ").replace("'", "").replace('"', '')

print(dataFilePath)
try:
    if dataFilePath.endswith('.csv'):
        dataFile = pd.read_csv(dataFilePath)
    elif dataFilePath.endswith('.xlsx'):
        dataFile = pd.read_excel(dataFilePath) #will add handling of .txt files later
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")
except Exception as e:
    print("Error loading file:", e)
    sys.exit()

# Display first few rows 
print("\nThe columns in your data are: \n", list(dataFile.columns))
print("\nFirst few rows are below\n\n", dataFile.head(6))

# Get pivot table dimensions from user
row_field = input("\nWhich category would you like to summarize?: ").upper().replace(" ", "")
col_field = input("\nWhich column would you like to group your data by?: ").upper().replace(" ", "")
val_field = input("\nWhich data points would you like to summarize?: ").upper().replace(" ", "")
agg_func = input("\nWhich aggregate function would you like to use (sum, mean, etc.)?: ").lower().replace(" ", "")

# Create pivot table
try:
    pivotTable = pd.pivot_table(
        dataFile,
        values=val_field,
        index=row_field,
        columns=col_field,
        aggfunc=agg_func,
        fill_value=0
    )
except Exception as e:
    print("Error creating pivot table:", e)
    sys.exit()

# Display pivot table
print("\n", agg_func, " of ", val_field, " by ", row_field, " and by ", col_field, "\n")
print(pivotTable)

# Data Visualization

plot_type = input("How would you like to visualize your data? (heatmap or bar plot): ").lower().replace(" ", "")

# Heatmap
if plot_type == 'heatmap':   
    ax = sns.heatmap(pivotTable, 
                annot=True, 
                cmap='crest'
                )
    ax.set(xlabel=row_field.capitalize(), ylabel=val_field.capitalize())
    plt.show()

# Bar Plot 
elif plot_type == 'barplot':
    ax = pivotTable.plot(kind='bar', figsize=(10,6), color=plt.get_cmap('Pastel1_r').colors)
    plot_title = agg_func.capitalize() + " " + val_field.lower() + " grouped by " + row_field.lower()
    plt.title(plot_title)
    plt.xlabel(row_field.capitalize())
    plt.ylabel(val_field.capitalize())
    plt.xticks(rotation=0, ha='center')
    plt.legend(title=col_field)
    plt.tight_layout()
    plt.show()

else:
    print("Unable to offer this option at the moment")

