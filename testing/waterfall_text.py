'''
Objective: test a waterfall
'''

from tlp_tools import create_teradata_engine
import pandas as pd
import dask.dataframe as dd
import polars as pl

from memory_line_profiler import profile