'''
Objective: Run various tests to determine the performance of various methods to upload a file to Teradata.

Functions to test:
    - teradataml.dataframe.copy_to.copy_to_sql
    - teradataml.dataframe.fastload.fastload
    - pd.DataFrame.to_sql

NOTE:
- All of these functions will use a pandas dataframe as the input.
'''

from memory_line_profiler import profile

from teradataml import create_context, remove_context
from teradataml.dataframe.copy_to import copy_to_sql
from teradataml.dataframe.fastload import fastload
import pandas as pd
from tlp_tools import create_teradata_engine

@profile
def create_engine():
    eng = create_teradata_engine()

    return eng

@profile
def read_csv():
    filename = ''
    df = pd.read_csv(filename)

    return df

@profile
def create_tera_context(eng):
    create_context(tdsqlengine=eng)

@profile
def remove_tera_context():
    remove_context()

@profile
def copy_to_sql_test(df, table_name):
    copy_to_sql(df, table_name=table_name, index=False, schema_name='user_work', if_exists='replace')

@profile
def fastload_test(df, table_name):
    fastload(df, table_name=table_name, index=False, schema_name='user_work', if_exists='replace')

@profile
def to_sql_test(df, table_name, eng):
    df.to_sql(table_name, eng, schema='user_work', if_exists='replace')

@profile
def main():
    eng = create_engine()
    df = read_csv()
    create_tera_context(eng)
    copy_to_sql(df, 'test')
    fastload(df, 'test')
    to_sql(df, 'test', eng)
    remove_tera_context()

if __name__ == '__main__':
    main()