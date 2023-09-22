import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, Normalize
import numpy as np
from lib import calc_desc_stat
from lib import boxplot_of_cols

def test_calc_desc_stat(dataset_col):
    
    df = pd.DataFrame({'data': [1, 2, 3, 4, 5]})
    if dataset_col is None: 
        return "Please input a dataframe column"
    out=dataset_col.describe()
    return out

    output = calc_desc_stat(df['data'])
    expected_output = df['data'].describe()

    assert output == expected_output

    with pytest.raises(TypeError):
        calc_desc_stat(None)

def test_boxplot_of_cols(df_wanted=None, col1=None, col2=None, col3=None, file_name=None):
    
    if isinstance(df_wanted, pd.DataFrame):
        print("good to go")
    else:
        return "This is the wrong input, you have " + str(type(df_wanted))
    list_of_columns = []
    if col1:
        list_of_columns.append(col1)
    if col2:
        list_of_columns.append(col2)
    if col3:
        list_of_columns.append(col3)
    if len(list_of_columns) == 0:
        print("There are no columns to plot")
        return
    
    df_to_plot = df_wanted[list_of_columns]  
    df_to_plot.boxplot()
    
    if file_name:
        plt.savefig(file_name)  
    # Save the figure before showing it
    plt.savefig("boxplot")
    plt.show()
    
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

    # Remove the boxplot file
    os.remove('boxplot.png')

  if __name__ == '__main__':
        test_calc_desc_stat()
        test_boxplot_of_cols()
