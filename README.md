# Hands-On-Data-Lab-Implementation
Developed a hands-on Python data analysis project using Pandas, NumPy, and Matplotlib to perform data cleaning, manipulation, statistical analysis, and visualization through practical exercises.
Hands-On Data Lab Implementation
1. Project Overview
This project provides a practical introduction to a Python-based data science environment. It demonstrates how to load, inspect, clean, manipulate, analyse, and visualize structured data using Python and common data science libraries.

The project uses a small sample sales dataset. If sales_data.csv is not available, the program creates it automatically, so the exercises can be run immediately.
2. Objectives Covered
The implementation follows the internship task objectives:
1. Set up a data science environment using Python and the required libraries.
2. Practise data manipulation using Pandas.
3. Create visualizations using Matplotlib.
4. Perform basic analysis and calculate summary statistics.
Jupyter Notebook can also be used to run the same Python code interactively. The provided main.py file is a script version of the lab.
3. Technologies Used
- Python 3.9 or newer – programming language.
- Jupyter Notebook – optional interactive environment.
- Pandas – reading, cleaning, filtering, sorting, and grouping data.
- NumPy – numerical operations and missing-value support.
- Matplotlib – creating charts and visualizations.
4. Project Structure
hands_on_data_lab/
├── main.py
├── README.md
├── sales_data.csv              # generated automatically if missing
└── outputs/
    ├── cleaned_sales_data.csv
    ├── revenue_by_product.png
    ├── units_by_region.png
    └── revenue_distribution.png
5. Installation and Environment Setup
Check that Python is installed:
python --version
Install the required libraries:
python -m pip install pandas numpy matplotlib
To install and use Jupyter Notebook as an interactive environment:
python -m pip install notebook
jupyter notebook
6. How to Run the Program
1. Open Terminal or a command prompt.
2. Move to the project directory.
3. Install the libraries listed above.
4. Run the program:
python main.py
On systems where Python is invoked as python3, use:
python3 main.py
The program creates a sample CSV file automatically if one does not exist. It then performs the lab exercises and saves the cleaned data and charts in the outputs directory.
7. Practical Exercises Demonstrated
Exercise 1: Load and inspect data
The program reads a CSV file with Pandas and displays the first five rows, dataset dimensions, data types, missing-value counts, and a statistical summary.
Exercise 2: Clean data
It removes duplicate rows, converts numeric columns, fills missing values, and prevents negative units and prices. A new revenue column is calculated using:

revenue = units_sold * unit_price
Exercise 3: Manipulate data
The program selects columns, filters records by revenue, sorts records, and groups data by product and region.
Exercise 4: Perform basic analysis
It calculates total units sold, total revenue, average revenue, highest revenue, and summary statistics. It also counts records by category.
Exercise 5: Visualize data
Matplotlib generates:
- revenue_by_product.png – total revenue for each product.
- units_by_region.png – units sold in each region.
- revenue_distribution.png – distribution of revenue values.
8. Dataset Description
Column	Description
date	Date of the sale
product	Product sold
category	Product category
units_sold	Number of units sold
unit_price	Price per unit in rupees
region	Sales region


The sample data is fictional and intended for learning and demonstration only. You may replace sales_data.csv with your own dataset while keeping the required column names.
9. Expected Result
After successful execution, the terminal displays dataset information, cleaned data, manipulation examples, and basic analysis results. The outputs folder contains the cleaned CSV file and three chart images.
10. Conclusion
This hands-on lab provides practical experience in setting up a Python data science environment and applying basic data science operations. It demonstrates data manipulation, cleaning, statistical analysis, and visualization using Pandas, NumPy, and Matplotlib. These skills form a foundation for more advanced data analysis and machine learning tasks.
11. References
- Python: https://docs.python.org/3/
- Jupyter: https://jupyter.org/documentation
- Pandas: https://pandas.pydata.org/docs/
- NumPy: https://numpy.org/doc/
- Matplotlib: https://matplotlib.org/stable/
