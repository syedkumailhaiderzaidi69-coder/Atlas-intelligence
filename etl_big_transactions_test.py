import pandas as pd


ZIP_FILE = "archive.zip"
CHUNK_SIZE = 10000


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


def test_big_file():

    print("Testing big transaction file...")

    chunk = next(
        pd.read_csv(
            ZIP_FILE,
            compression="zip",
            chunksize=CHUNK_SIZE,
            usecols=USEFUL_COLUMNS
        )
    )

    print("Test load successful.")
    print(f"Rows loaded: {len(chunk)}")
    print(f"Columns loaded: {len(chunk.columns)}")
    print(chunk.head())
    print(chunk.info())


if __name__ == "__main__":

    test_big_file()
