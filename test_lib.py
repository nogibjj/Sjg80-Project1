import pandas as pd
import pytest
import matplotlib.pyplot as plt
from lib import calc_desc_stat
from lib import boxplot_of_cols

def test_calc_desc_stat():
    
    df = pd.DataFrame({'data': [1, 2, 3, 4, 5]})
    output = calc_desc_stat(df['data'])
    expected_output = df['data'].describe()
    assert output == expected_output

def test_boxplot_of_cols():

    # Create a DataFrame with some data
    df = pd.DataFrame({'data1': [1, 2, 3, 4, 5], 'data2': [6, 7, 8, 9, 10]})

    # Test with a valid input
    boxplot_of_cols(df, col1='data1', col2='data2', file_name='boxplot.png')

    # Test with an invalid input
    with pytest.raises(TypeError):
        boxplot_of_cols(None)

    # Test with a DataFrame that has no columns to plot
    with pytest.raises(SystemExit):
        boxplot_of_cols(df, col1=None, col2=None, col3=None)

    # Check if the boxplot was saved correctly
    assert plt.imread('boxplot.png').shape == (400, 600)

if __name__ == '__main__':
    test_calc_desc_stat()
    test_boxplot_of_cols()
