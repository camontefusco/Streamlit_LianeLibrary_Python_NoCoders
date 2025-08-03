# library_connection.py

import pandas as pd
from sqlalchemy import create_engine, text
import getpass

# --- Database Credentials ---
schema = "lianes_library"
host = "127.0.0.1"
user = "root"
port = 3306
engine = None  # Initialize engine as None

# --- Create Engine (runs only once on import) ---
try:
    password = getpass.getpass(prompt='Enter your MySQL password: ')
    connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'
    
    # Global engine for all queries
    engine = create_engine(connection_string)

    # Optional: Test the connection
    engine.connect().close()
    print("✅ Database engine created successfully.")

except Exception as error:
    print(f'❌ ERROR: Could not create database engine.\n{error}')

# --- Query Helpers ---

def run_query(query, params=None):
    with engine.connect() as connection:
        result = connection.execute(text(query), params or {})
        if result.returns_rows:
            return pd.DataFrame(result.fetchall(), columns=result.keys())
        return None

def execute_command(query, params=None):
    with engine.begin() as connection:
        connection.execute(text(query), params or {})

