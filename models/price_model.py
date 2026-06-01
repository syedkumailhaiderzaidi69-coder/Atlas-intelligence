from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

import pandas as pd


def train_price_models(df):

    required_cols = [
        "Investment Score",
        "Projected Growth",
        "Rental Yield",
        "Average Price"
    ]

    if not all(col in df.columns for col in required_cols):

        return None

    ml_df = df.copy()

    ml_df = ml_df.dropna(
        subset=required_cols
    )

    X = ml_df[[
        "Investment Score",
        "Projected Growth",
        "Rental Yield"
    ]]

    y = ml_df["Average Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    linear_model = LinearRegression()

    linear_model.fit(
        X_train,
        y_train
    )

    linear_pred = linear_model.predict(
        X_test
    )

    forest_model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    forest_model.fit(
        X_train,
        y_train
    )

    forest_pred = forest_model.predict(
        X_test
    )

    linear_r2 = r2_score(
        y_test,
        linear_pred
    )

    linear_mae = mean_absolute_error(
        y_test,
        linear_pred
    )

    forest_r2 = r2_score(
        y_test,
        forest_pred
    )

    forest_mae = mean_absolute_error(
        y_test,
        forest_pred
    )

    if forest_r2 >= linear_r2:

        best_model = forest_model
        best_model_name = "Random Forest"

    else:

        best_model = linear_model
        best_model_name = "Linear Regression"

    model_results = pd.DataFrame({
        "Model": [
            "Linear Regression",
            "Random Forest"
        ],
        "R² Score": [
            round(linear_r2, 2),
            round(forest_r2, 2)
        ],
        "Mean Absolute Error": [
            f"AED {linear_mae:,.0f}",
            f"AED {forest_mae:,.0f}"
        ]
    })

    importance_df = pd.DataFrame({
        "Feature": X.columns,
        "Impact": forest_model.feature_importances_
    })

    importance_df["Impact"] = (
        importance_df["Impact"]
        .round(3)
    )

    return {
        "best_model": best_model,
        "best_model_name": best_model_name,
        "model_results": model_results,
        "importance_df": importance_df
    }
