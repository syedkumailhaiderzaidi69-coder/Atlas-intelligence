import pandas as pd
from sqlalchemy import create_engine
import os


CSV_FILE = "dubai_clean_ready.csv"


def clean_data(file_path):
    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip()

    if "Price" in df.columns:
        df["Price"] = pd.to_numeric(
            df["Price"],
            errors="coerce"
        )

    if "Projected Growth" in df.columns:
        df["Projected Growth"] = pd.to_numeric(
            df["Projected Growth"],
            errors="coerce"
        )

    if "Investment Score" in df.columns:
        df["Investment Score"] = pd.to_numeric(
            df["Investment Score"],
            errors="coerce"
        )

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce"
        )

    df = df.dropna(
        subset=[
            "Area",
            "Price",
            "Projected Growth",
            "Investment Score"
        ]
    )

    return df


def load_to_database(df):
    database_url = os.getenv("DATABASE_URL")

    if database_url is None:
        raise ValueError("DATABASE_URL environment variable not found.")

    engine = create_engine(database_url)

    df.to_sql(
        "dubai_properties",
        engine,
        if_exists="replace",
        index=False
    )

    print("ETL completed successfully.")
    print(f"Rows loaded: {len(df)}")


if __name__ == "__main__":
    clean_df = clean_data(CSV_FILE)
    load_to_database(clean_df)
