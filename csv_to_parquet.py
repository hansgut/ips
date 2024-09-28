import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Read the CSV file

df = pd.read_csv('TRAIN_DATA.csv')

# Write the DataFrame to a Parquet file

pq.write_table(pa.Table.from_pandas(df), 'TRAIN_DATA.parquet')
