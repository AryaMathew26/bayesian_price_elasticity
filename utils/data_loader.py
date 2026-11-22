
"""
data_loader.py

This module centralises data loading and basic validation.

In the original R project, the data is loaded using:

    iphone_case_daily_sales_tbl <- read_csv("data/iphone_case_daily_sales.csv")

In Python, we use pandas instead. Keeping the loading logic in one file
means every model uses the same dataset and the same validation rules.
"""

from pathlib import Path

import pandas as pd


# PROJECT_ROOT points to the main project folder:
# bayesian_price_elasticity_python/
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# The dataset lives inside the project data/ folder.
DATA_DIR = PROJECT_ROOT / "data"

# Full path to the CSV file.
DATA_FILE = DATA_DIR / "iphone_case_daily_sales.csv"


def load_sales_data() -> pd.DataFrame:
    """
    Load the iPhone case sales dataset.

    Returns
    -------
    pd.DataFrame
        A dataframe containing at least these columns:
        - product
        - unit_price
        - quantity

    Raises
    ------
    FileNotFoundError
        If the CSV file is missing.
    ValueError
        If required columns are missing.
    """

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Could not find the data file at {DATA_FILE}. "
            "Make sure iphone_case_daily_sales.csv is inside the data folder."
        )

    # pandas read_csv is the direct Python equivalent of readr::read_csv().
    df = pd.read_csv(DATA_FILE)

    # These are the columns used by Model 1 and later models.
    required_columns = {"product", "unit_price", "quantity"}

    missing_columns = required_columns.difference(df.columns)

    if missing_columns:
        raise ValueError(
            "The dataset is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    # Make sure the numeric columns are actually numeric.
    # errors="raise" makes pandas fail clearly if conversion is impossible.
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="raise")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="raise")

    # Product is treated as a categorical/grouping variable in later models.
    df["product"] = df["product"].astype("category")

    return df


def inspect_data(df: pd.DataFrame) -> None:
    """
    Print a simple inspection report for the dataset.

    This plays a similar role to skim() in the original R workflow.
    """

    print("=" * 72)
    print("First five rows")
    print("=" * 72)
    print(df.head())

    print("\n" + "=" * 72)
    print("Column types and non-null counts")
    print("=" * 72)
    print(df.info())

    print("\n" + "=" * 72)
    print("Summary statistics")
    print("=" * 72)
    print(df.describe(include="all"))
