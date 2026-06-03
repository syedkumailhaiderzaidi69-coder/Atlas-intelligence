import duckdb
import pandas as pd

# Use a relative path to your zip file in the repo
file_path = "archive.zip"

# Connect to in-memory DuckDB
con = duckdb.connect(database=':memory:')

# Load CSV directly from ZIP
query = f"""
CREATE TABLE dubai_full AS
SELECT *
FROM read_csv_auto('{file_path}', COMPRESSION='zip');
"""

con.execute(query)

# Optional: preview
df = con.execute("SELECT * FROM dubai_full LIMIT 5").df()
print(df.head())
