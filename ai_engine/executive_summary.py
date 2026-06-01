def generate_executive_summary(question, result_df):

    question = question.lower()

    if result_df is None or result_df.empty:

        return "No results were found for this query."

    first_row = result_df.iloc[0]

    if "rental yield" in question or "yield" in question:

        area = first_row["Area"]
        value = first_row.iloc[1]

        return (
            f"{area} currently shows the strongest rental yield performance "
            f"at approximately {value:.1f}%. This suggests strong passive income "
            f"potential for rental-focused investors."
        )

    elif "growth" in question:

        area = first_row["Area"]
        value = first_row.iloc[1]

        return (
            f"{area} currently shows the strongest projected growth momentum "
            f"at approximately {value:.1f}%. This may indicate stronger long-term "
            f"capital appreciation potential."
        )

    elif "investment" in question or "score" in question:

        area = first_row["Area"]
        value = first_row.iloc[1]

        return (
            f"{area} currently ranks highest based on Atlas investment scoring "
            f"with a score of approximately {value:.1f}. This indicates a stronger "
            f"overall investment profile compared to other analyzed communities."
        )

    else:

        return (
            "Atlas Intelligence generated this result based on the selected query. "
            "The top-ranked area represents the strongest signal within the current dataset."
        )
