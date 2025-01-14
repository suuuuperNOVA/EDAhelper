# Checking statistics are calculated correctly by the function and both matrices have correct values
import pandas as pd
import numpy as np
import statistics
from EDAhelper.column_stats import column_stats


def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance


def test_column_args_in_outputs():
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    cols = ('petal_width', 'petal_length')
    assert column_stats(iris, cols)[1][cols[1]].index[0] == cols[0], 'Column names do not match'
    assert column_stats(iris, cols)[1][cols[1]].index[1] == cols[1], 'Column names do not match'
    assert column_stats(iris, cols)[2][cols[1]].index[0] == cols[0], 'Column names do not match'
    assert column_stats(iris, cols)[2][cols[1]].index[1] == cols[1], 'Column names do not match'
    

def test_column_values_calculated():
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    cols = ('petal_width', 'petal_length')
    assert column_stats(iris, cols)[0]['Mean'][0] == round(iris['petal_width'].sum()/iris['petal_width'].count(), 3), 'Incorrect Mean calculation'
    assert column_stats(iris, cols)[0]['Var'][0] - 0.5 <= variance(iris['petal_width']) <= column_stats(iris, ('petal_width', 'petal_length'))[0]['Var'][0] + 0.5, 'Incorrect Median Calculation'
    
def test_cov_matrix_diag():
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    cols = ('petal_width', 'petal_length')
    assert round(column_stats(iris, cols)[1]['petal_width'][0]) == 1, 'Covariance calculated incorrectly'
    assert round(column_stats(iris, cols)[1]['petal_length'][1]) == 1, 'Covariance calculated incorrectly'

def test_num_cols():
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    cols = ('petal_width', 'petal_length')
    assert len(column_stats(iris, cols)[0].columns) == 9
    assert len(cols) == len(column_stats(iris, cols)[0])
    assert len(cols) == len(column_stats(iris, cols)[1])
    assert len(cols) == len(column_stats(iris, cols)[2])

