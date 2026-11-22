"""
Hands-On Data Lab Implementation
--------------------------------
A beginner-friendly practical data analysis lab.

This program demonstrates:
1. Setting up and using a Python data science environment
2. Creating and loading a dataset with Pandas
3. Inspecting and manipulating tabular data
4. Handling missing values and duplicate rows
5. Performing basic statistical analysis
6. Creating visualizations with Matplotlib

If sales_data.csv is not present, a sample dataset is created automatically.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


DATA_FILE = Path("sales_data.csv")
OUTPUT_DIR = Path("outputs")


def create_sample_dataset(path: Path) -> None:
    """Create a sample sales dataset for practice."""
    data = {
        "date": [
            "2026-01-03", "2026-01-05", "2026-01-08", "2026-01-12",
            "2026-01-15", "2026-01-18", "2026-01-21", "2026-01-24",
            "2026-01-27", "2026-01-30", "2026-02-02", "2026-02-05"
        ],
        "product": [
            "Laptop", "Phone", "Tablet", "Laptop", "Phone", "Headphones",
            "Tablet", "Laptop", "Headphones", "Phone", "Tablet", "Laptop"
        ],
        "category": [
            "Electronics", "Electronics", "Electronics", "Electronics",
            "Electronics", "Accessories", "Electronics", "Electronics",
            "Accessories", "Electronics", "Electronics", "Electronics"
        ],
        "units_sold": [2, 5, 3, 1, 4, 8, 2, 3, 6, 2, 4, 2],
        "unit_price": [55000, 22000, 18000, 55000, 22000, 1500,
                       18000, 55000, 1500, 22000, 18000, 55000],
        "region": [
            "North", "South", "East", "West", "North", "South",
            "East", "West", "North", "South", "East", "West"
        ],
    }

    df = pd.DataFrame(data)
    # Add a missing value to demonstrate the cleaning exercise.
    df.loc[10, "region"] = np.nan
    df.to_csv(path, index=False)
    print(f"Sample dataset created: {path}")


def load_dataset(path: Path) -> pd.DataFrame:
    """Load the CSV dataset, creating it if necessary."""
    if not path.exists():
        create_sample_dataset(path)

    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df


def inspect_dataset(df: pd.DataFrame) -> None:
    """Display an overview of the dataset."""
    print("\n========== DATASET OVERVIEW ==========")
    print("\nFirst five rows:")
    print(df.head())

    print("\nDataset shape (rows, columns):")
    print(df.shape)

    print("\nColumn data types:")
    print(df.dtypes)

    print("\nMissing values in each column:")
    print(df.isnull().sum())

    print("\nBasic statistical summary:")
    print(df.describe(include="all"))


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicates and handle missing or invalid values."""
    cleaned = df.copy()
    cleaned.columns = cleaned.columns.str.strip().str.lower()

    cleaned = cleaned.drop_duplicates()
