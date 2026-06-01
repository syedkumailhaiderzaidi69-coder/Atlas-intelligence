def generate_sql_from_question(question):

    question = question.lower()

    if "best rental yield" in question:

        return """
SELECT Area,
AVG("Rental Yield") AS rental_yield
FROM df
GROUP BY Area
ORDER BY rental_yield DESC
LIMIT 10
"""

    elif "highest investment score" in question:

        return """
SELECT Area,
AVG("Investment Score") AS investment_score
FROM df
GROUP BY Area
ORDER BY investment_score DESC
LIMIT 10
"""

    elif "highest growth" in question:

        return """
SELECT Area,
AVG("Projected Growth") AS projected_growth
FROM df
GROUP BY Area
ORDER BY projected_growth DESC
LIMIT 10
"""

    else:

        return """
SELECT Area,
AVG("Investment Score") AS investment_score
FROM df
GROUP BY Area
ORDER BY investment_score DESC
LIMIT 10
"""
