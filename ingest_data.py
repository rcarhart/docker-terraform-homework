
import os
import pandas as pd
from sqlalchemy import create_engine


connection_string = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string)

df = pd.read_csv("green_tripdata_2019-10.csv")
print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))
df.to_sql("green_tripdata_2019_01", engine, if_exists="replace", index=False)