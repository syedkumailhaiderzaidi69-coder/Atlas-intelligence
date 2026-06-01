def classify_market_risk(avg_growth):

    if avg_growth >= 10:

        return "Stable / Lower Risk"

    elif avg_growth >= 7:

        return "Moderate Risk"

    else:

        return "Higher Volatility"


def generate_investment_strategy(

    avg_growth,
    best_yield_value

):

    if (

        avg_growth >= 10
        and best_yield_value >= 7

    ):

        strategy = (
            "Balanced Growth + Rental Income"
        )

        reason = (
            "Atlas Intelligence detects strong appreciation potential combined with attractive rental yield performance."
        )

    elif avg_growth >= 10:

        strategy = (
            "Long-Term Capital Appreciation"
        )

        reason = (
            "Growth indicators suggest strong long-term value appreciation opportunities across selected Dubai communities."
        )

    elif best_yield_value >= 7:

        strategy = (
            "High Rental Yield Acquisition"
        )

        reason = (
            "Atlas Intelligence detects strong passive income potential from rental-focused investment opportunities."
        )

    else:

        strategy = (
            "Stable Defensive Investment"
        )

        reason = (
            "Current market conditions indicate balanced and lower-risk investment positioning."
        )

    return strategy, reason
