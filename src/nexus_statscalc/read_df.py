import pandas as pd

def read_df(path):
    df = pd.read_excel(path)
    df['timeStamp'] = pd.to_datetime(df['timeStamp'])
    #TODO: iterate through all variables
    #name_list = df['name'].unique()
    #df = df[df['name']==name_list[0]]
    return df

def get_variable_names(df):
    name_list = df['name'].unique()
    return name_list