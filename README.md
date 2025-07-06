# Pivot Table Program

This Python-based Pivot Table Program allows users to load a dataset (CSV or Excel), create customizable pivot tables, and visualize patterns using **interactive heatmaps** or **grouped bar plots**.

---

## Features

- Load `.csv` or `.xlsx` datasets
- Choose any column as:
  - **Index (row labels)**
  - **Columns (grouping)**
  - **Values (data to summarize)**
- Select common aggregation functions like `sum`, `mean`, etc.
- Display pivot tables in the terminal
- Visualize results with:
  - **Grouped Bar Plot** (using `matplotlib`)
  - **Heatmap** (using `seaborn`)

---

## Requirements

- Python 3.7+
- `pandas`
- `matplotlib`
- `seaborn`

Install requirements:

```bash
pip install pandas matplotlib seaborn
````

---

## How to Use

1. **Run the script**:

   ```bash
   python main.py
   ```

2. **Follow prompts** to:

   * Enter the file path to your dataset
   * Select columns for summarization
   * Choose an aggregation function (e.g., `sum`, `mean`)
   * Pick a visualization type (`heatmap` or `barplot`)

---

## Example

```
Please enter your data file path here: /Users/yasmina/Documents/sales_data.csv

Which category would you like to summarize?: produc tline
Which column would you like to group your data by?: dealsize
Which data points would you like to summarize?: sales
Which aggregate function would you like to use (sum, mean, etc.)?: sum

How would you like to visualize your data? (heatmap or bar plot): heatmap
```

---

## Notes

* Column names are **case-insensitive** and will have spaces removed automatically.
* The program handles most data formatting issues, but expects clean tabular data.
* Currently supports only `.csv` and `.xlsx` formats.

---

## Incoming updates

* [ ] Add support for `.txt` and `.json` files
* [ ] Export pivot tables to Excel
* [ ] Add interactive Plotly visualizations with hover support
* [ ] Produce a downloadable detailed report

---

## Author

Yasmina Traoré

