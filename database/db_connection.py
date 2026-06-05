from sqlalchemy import create_engine
import pandas as pd

def get_database_connection():
    # Replace with your Supabase connection URL
    DATABASE_URL = "postgresql://postgresql://postgres.wzfyczdilwsiicaihcgh:Nvidia67890---@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres"
    
    engine = create_engine(DATABASE_URL)
    return engine

def load_full_transactions():
    engine = get_database_connection()
    query = "SELECT * FROM dubai_transactions_master"
    df = pd.read_sql(query, engine)
    return df
