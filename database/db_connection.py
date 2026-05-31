import streamlit as st

from sqlalchemy import create_engine


@st.cache_resource

def get_database_connection():

    DATABASE_URL = st.secrets["DATABASE_URL"]

    engine = create_engine(
        DATABASE_URL
    )

    return engine
