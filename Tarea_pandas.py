import pandas as pd

def read_pandas(filepath, names):
    '''
    Docstring
    '''
    df = pd.read_csv(filepath, names=names)
    return df

def main():
    # Cvs path
    filepath = './data/iris.data'
    # Column titles
    names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

    df = read_pandas(filepath, names)
    
    # Data frame 
    print(df)

    # The first 20 items in the data frame
    print(df.head(20)) 

    # The last 20 items in the data frame
    print(df.tail(20))

    # Data fram without the petal width column
    df_mpw = df.drop(columns='petal_width')
    print(df_mpw)

    # Create a new column adding two existing columns
    df['sp_l + pt_l'] = df['sepal_length'] + df['petal_length']
    print(df)

    # Describe
    # If the column that we are trying to describe is full of numbers it will gives us the count, the mean, the standard deviation, the min and max value, etc...
    print(df['sepal_length'].describe()) 
    # Else if it's a column full of strings the count, the number of unique entries, the most popular value, and how may times it appears
    print(df['class'].describe()) 

    # Type 
    # To know the value of the items that are in each column we use the keyword "dtype" 
    print(df.dtypes)
    

if __name__ == "__main__":

    main()
    