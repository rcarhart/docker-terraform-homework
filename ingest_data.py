
import os
import pandas as pd
from sqlalchemy import create_engine


connection_string = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string)

import os
import pandas as pd
from sqlalchemy import create_engine, inspect

connection_string = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string)

# Check if the table exists
try:
    inspector = inspect(engine)

    # Check and process 'green_tripdata_2019_01' table
    if not inspector.has_table("green_tripdata_2019_01"):
        print("Table 'green_tripdata_2019_01' does not exist. Creating table and ingesting data.")
        df = pd.read_csv("green_tripdata_2019-10.csv")
        df.to_sql("green_tripdata_2019_01", engine, if_exists="replace", index=False)
    else:
            print("Table 'green_tripdata_2019_01' already has data. Doing nothing.")

    # Check and process 'taxi_zone_lookup' table
    if not inspector.has_table("taxi_zone_lookup"):
        print("Table 'taxi_zone_lookup' does not exist. Creating table and ingesting data.")
        df_taxi_zone_lookup = pd.read_csv("taxi_zone_lookup.csv")
        df_taxi_zone_lookup.to_sql("taxi_zone_lookup", engine, if_exists="replace", index=False)
    else:
            print("Table 'taxi_zone_lookup' already has data. Doing nothing.")

except Exception as e:
    print(f"An error occurred: {e}")