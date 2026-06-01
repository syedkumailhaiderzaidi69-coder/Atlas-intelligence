import pandas as pd
from sqlalchemy import create_engine
import os


ZIP_FILE = "archive.zip"
CSV_FILE_IN_ZIP = "Transactions.csv"
CHUNK_SIZE = 50000


USEFUL_COLUMNS = [
    "transaction_id",
    "procedure_name_en",
    "instance_date",
    "property_type_en",
    "property_sub_type_en",
    "property_usage_en",
    "area_name_en",
    "building_name_en",
    "project_name_en",
    "master_project_en",
    "nearest_landmark_en",
    "nearest_metro_en",
    "nearest_mall_en",
    "rooms_en",
    "has_parking",
    "procedure_area",
    "actual_worth",
    "meter_sale_price",
    "rent_value",
    "meter_rent_price"
]


COLUMN_RENAME_MAP = {
    "transaction_id": "Transaction ID",
    "procedure_name_en": "Transaction Type",
    "instance_date": "Date",
    "property_type_en": "Property Type",
    "property_sub_type_en": "Property Sub Type",
    "property_usage_en": "Property Usage",
    "area_name_en": "Area",
    "building_name_en": "Building",
    "project_name_en": "Project",
    "master_project_en": "Master Project",
    "nearest_landmark_en": "Nearest Landmark",
    "nearest_metro_en": "Nearest Metro",
    "nearest_mall_en": "Nearest Mall",
    "rooms_en": "Rooms",
    "has_parking": "Parking",
    "procedure_area": "Area Size",
    "actual_worth": "Price",
    "meter_sale_price": "Price per sqm",
    "rent_value": "Rent Value",
    "meter_rent_price": "Rent per sqm"
}


def clean_chunk(chunk):

    chunk = chunk[USEFUL_COLUMNS].copy()

    chunk = chunk.rename(
        columns=COLUMN_RENAME_MAP
    )

    chunk["Date"] = pd.to_datetime(
        chunk["Date"],
        errors="coerce"
    )

    numeric_columns = [
        "Area Size",
        "Price",
        "Price per sqm",
        "Rent Value",
        "Rent per sqm"
    ]

    for col in numeric_columns:

        chunk[col] = pd.to_numeric(
            chunk[col],
            errors="coerce"
        )

    chunk = chunk.dropna(
        subset=[
            "Area",
            "Date",
            "Price"
        ]
    )

    chunk = chunk[
        chunk["Price"] > 0
    ]

    return chunk


def load_big_transactions():

    database_url = os.getenv("DATABASE_URL")

    if database_url is None:

        raise ValueError(
            "DATABASE_URL environment variable not found."
        )

    engine = create_engine(
        database_url
    )

    first_chunk = True

    total_rows = 0

    for chunk in pd.read_csv(
        ZIP_FILE,
        compression="zip",
        chunksize=CHUNK_SIZE,
        usecols=USEFUL_COLUMNS
    ):

        clean_df = clean_chunk(
            chunk
        )

        if first_chunk:

            clean_df.to_sql(
                "dubai_transactions_master",
                engine,
                if_exists="replace",
                index=False
            )

            first_chunk = False

        else:

            clean_df.to_sql(
                "dubai_transactions_master",
                engine,
                if_exists="append",
                index=False
            )

        total_rows += len(clean_df)

        print(
            f"Loaded {total_rows:,} cleaned rows so far..."
        )

    print(
        f"Big ETL completed successfully. Total rows loaded: {total_rows:,}"
    )


if __name__ == "__main__":

    load_big_transactions()
