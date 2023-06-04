import sqlite3
from memory_line_profiler import profile
import pandas as pd 

@profile
def main():
    conn = sqlite3.connect('sample.db')
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    iris.to_sql('iris', conn, if_exists='replace', index=False)

@profile
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

@profile
def cached_factorial(n):
    return factorial(n)


if __name__ == '__main__':
    main()
    cached_factorial(100000)
