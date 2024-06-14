import pandas as pd
def preprocess(df):
    """
    Preprocess the data removing uncessary data and setting elements to their correct types
    Handle Null values by backward fill null values
    """
    df.drop(['Unnamed: 0'], axis=1, inplace=True)#remove empty column
    df.drop(['type'], axis=1, inplace=True) #remove type column as highly correlated with size column. Size has more detail
    df['Date'] = pd.to_datetime(df['Date']) #update column from string to datetime
    df.set_index('Date', inplace=True) 
    df.fillna(method='bfill', inplace=True)
    return df


#TODO: Need to add in lag variables to the data preprcessing function