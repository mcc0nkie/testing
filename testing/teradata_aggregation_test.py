'''
Objective: test various methods performed on data downloaded from Teradata.
'''

from tlp_tools import create_teradata_engine
import pandas as pd
import dask.dataframe as dd
import polars as pl

from memory_line_profiler import profile

@profile
def pandas_test(eng, query):
    '''
    Objective: test pandas performance
    '''
    df = pd.read_sql(query, eng)

    # do stuff with df

    df.to_parquet('pandas_test.parquet')
    df.to_feather('pandas_test.feather')
    df.to_hdf('pandas_test.hdf', key='df', mode='w')
    return df

@profile
def dask_test(eng, query):
    '''
    Objective: test dask performance
    '''
    df = dd.read_sql(query, eng)

    # do stuff with df

    df.to_parquet('dask_test.parquet')
    df.to_feather('dask_test.feather')
    df.to_hdf('dask_test.hdf', key='df', mode='w')
    return df

@profile
def polars_test(eng, query):
    '''
    Objective: test polars performance
    '''
    df = pl.read_sql(eng, query)

    # do stuff with df

    df.to_parquet('polars_test.parquet')
    df.to_feather('polars_test.feather')
    df.to_hdf('polars_test.hdf', key='df', mode='w')
    return df

if __name__ == '__main__':
    eng = create_teradata_engine()
    query = 'SELECT * FROM database.table'

    pandas_test(eng, query)
    dask_test(eng, query)
    polars_test(eng, query)