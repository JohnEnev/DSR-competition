import pandas as pd

def merge(df_train, df_store):
    '''
    Merge train data with store data based on
    values in Stores column
    '''
    full_df = df_train.merge(df_store, how='left', on='Store')
    return full_df

def drop_column(df, column='Customers'):
    '''
    Remove the Customers column as instructed by competition instructors.
    '''
    df_new = df.drop(str(column), axis=1)
    return df_new

def drop_null_targets(df, target='Sales'):
    '''
    Remove the null targets (i.e. Sales)
    '''
    null_target = df[df[str(target)].isnull()]
    df_new = df[~df.index.isin(null_target.index)]
    return df_new

def drop_null_features(df, threshold=0.03, verbose=True):
    '''
    Remove the null features if number of rows with null feature is
    less than a certain percentage of the full data rows
    '''
    tot_rows = df.shape[0]
    if verbose:
        print("Total number of rows in full data set: ", tot_rows)
    for column in df.columns:
        null_rows = df.loc[df.loc[:, str(column)].isnull()].shape[0]
        frac = null_rows / tot_rows
        if verbose:
            print(f"Number of rows with null {str(column)}: {null_rows} ({frac * 100 : .0f}% of full data).")
        if frac > 0 and frac <= threshold:
            df = df.loc[~df.loc[:, str(column)].isnull()]
            if verbose:
                print(f"Removed rows with null {str(column)}.")
    if verbose:
        print("Total number of rows in clean data set: ", df.shape[0])
    return df


