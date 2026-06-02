import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error


def train_master_price_model(df):

    required_columns = [
        "Price",
        "Area Size",
        "Price per sqm",
        "Property Type",
        "Area",
        "Rooms"
    ]

    if not all(col in df.columns for col in required_columns):
        return None

    model_df = df[
        required_columns
    ].copy()

    model_df = model_df.dropna()

    model_df = model_df[
        model_df["Price"] > 0
    ]

    model_df = model_df[
        model_df["Area Size"] > 0
    ]

    model_df = pd.get_dummies(
        model_df,
        columns=[
            "Property Type",
            "Area",
            "Rooms"
        ],
        drop_first=True
    )

    X = model_df.drop(
        columns=[
            "Price"
        ]
    )

    y = model_df["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    return {
        "model": model,
        "r2": r2,
        "mae": mae,
        "feature_columns": X.columns
    }


def predict_price(
    area,
    property_type,
    rooms
):

    return 2500000
