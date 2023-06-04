import pandas as pd
import dask.dataframe as dd
import polars as pl
from tlp_tools import create_teradata_engine
from memory_line_profiler import profile
import pyarrow.parquet as pq

# Function #1: Pandas
@profile
def pandas_func():
    # Read SQL Query
    df = pd.read_sql_query(query, engine)
    # Save to parquet
    df.to_parquet('pandas.parquet')
    # Read from parquet
    df = pd.read_parquet('pandas.parquet')
    
    # Perform operations
    df['column1']  # Column selection
    df[10:20]  # Row selection
    df[df['column1'] > 50]  # Filtering
    df.sort_values('column1')  # Sorting
    df.groupby('column1').sum()  # Grouping
    df.merge(df, on='column1')  # Merging
    df['column1'].value_counts()  # Value counts
    df.duplicated(subset=['column1', 'column2'])  # Duplicated
    df.drop_duplicates(subset=['column1', 'column2'])  # Drop duplicates
    df.fillna(0)  # Missing values
    df['column1'].astype('str')  # Type casting
    df['column1'].apply(lambda x: x**2)  # Applying functions
    df['column1'].str.lower()  # String operations
    pd.to_datetime(df['column1']).dt.year  # Date/Time operations
    pd.cut(df['column1'], bins=5)  # Binning data
    df.melt(id_vars=['column1'], value_vars=['column2'])  # Reshaping data
    df['column1'].describe()  # Descriptive statistics
    df['column1'] + df['column2']  # Vectorized operations
    
    # Save final results
    df.to_parquet('pandas_final.parquet')

# Function #2: Dask
@profile
def dask_func():
    # Read SQL Query
    df = dd.read_sql_table('your_table', engine, index_col='your_index_column')
    # Save to parquet
    df.to_parquet('dask.parquet')
    # Read from parquet
    df = dd.read_parquet('dask.parquet')

    # Perform operations
    df['column1']  # Column selection
    df.loc[10:20]  # Row selection
    df[df['column1'] > 50]  # Filtering
    df.sort_values('column1')  # Sorting
    df.groupby('column1').sum().compute()  # Grouping
    df.merge(df, on='column1')  # Merging
    df['column1'].value_counts().compute()  # Value counts
    df.duplicated(subset=['column1', 'column2']).compute()  # Duplicated
    df.drop_duplicates(subset=['column1', 'column2']).compute()  # Drop duplicates
    df.fillna(0)  # Missing values
    df['column1'].astype('str')  # Type casting
    df['column1'].apply(lambda x: x**2, meta=('column1', 'int64')).compute()  # Applying functions
    df['column1'].str.lower()  # String operations
    dd.to_datetime(df['column1']).dt.year  # Date/Time operations
    dd.cut(df['column1'], bins=5)  # Binning data
    df.categorize(columns=['column1']).pivot_table(index='column1', columns='column2')  # Reshaping data
    df['column1'].describe().compute()  # Descriptive statistics
    df['column1'] + df['column2']  # Vectorized operations

    # Save final results
    df.to_parquet('dask_final.parquet')

# Function #3: Polars
@profile
def polars_func():
    # Read SQL Query
    df = pl.scan_sql('your_table', engine)
    # Save to parquet
    df.write_parquet('polars.parquet')
    # Read from parquet
    df = pl.scan_parquet('polars.parquet')
    
    # Perform operations
    df['column1']  # Column selection
    df.slice(10, 10)  # Row selection
    df.filter(col('column1') > 50)  # Filtering
    df.sort('column1')  # Sorting
    df.groupby('column1').agg([col('column2').sum()])  # Grouping
    df.join(df, on='column1')  # Merging
    df['column1'].value_counts()  # Value counts
    df.drop_duplicates(subset=['column1', 'column2'])  # Drop duplicates
    df.fill_none('column1', 0)  # Missing values
    df.with_column(df['column1'].cast(pl.Int32))  # Type casting
    df.with_column(df['column1'].apply(lambda x: x**2))  # Applying functions
    df.with_column(df['column1'].str.lower())  # String operations
    df.with_column(pl.col('column1').str.strptime(pl.Date))  # Date/Time operations
    df.with_column(pl.col('column1').apply_buckets(pl.bucketizer([0, 50, 100])))  # Binning data
    df.melt(id_vars=['column1'], value_vars=['column2'])  # Reshaping data
    df.describe()  # Descriptive statistics
    df.with_column(df['column1'] + df['column2'])  # Vectorized operations
    
    # Save final results
    df.write_parquet('polars_final.parquet')


if __name__ == '__main__':
    # Create Teradata Engine
    engine = create_teradata_engine()

    # SQL Query
    query = """
    SELECT *
    FROM your_table
    """

    # Run functions
    pandas_func()
    dask_func()
    polars_func()
