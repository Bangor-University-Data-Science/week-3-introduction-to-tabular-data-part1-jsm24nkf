import pandas as pd

def create_summary_table(df):
    summary = {
        'Feature Name': df.columns,
        'Data Type': df.dtypes.values,
        'Has Missing Values?': df.isnull().any().values,
        'Number of Unique Values': df.nunique().values
    }

    return pd.DataFrame(summary)
