import pandas as pd 
import matplotlib.pyplot as plt


def calc_desc_stat(dataset_col):
    if dataset_col is None: 
        return "Please input a dataframe column"
    out=dataset_col.describe()
    return out

def boxplot_of_cols(df_wanted=None, col1=None, col2=None, col3=None, file_name=None):
    
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

if __name__ == "__main__":
