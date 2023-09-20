import numpy as np
import pandas as pd
import re


def add_datepart(df, col, drop=False):
    """
    Extract all pieces of the datetime object into columns
    :param df: DataFrame
    :param col: The column that is the timestamp
    :param drop: Delete the existing timestamp column
    :return:
    """
    fld = df[col]
    if not np.issubdtype(fld.dtype, np.datetime64):
        df[col] = fld = pd.to_datetime(fld, infer_datetime_format=True)
    targ_pre = re.sub('[Dd]ate$', '', col)
    for n in ('Year', 'Month', 'Week', 'Day',
              'Dayofweek', 'Dayofyear',
              'Is_month_end', 'Is_month_start',
              'Is_quarter_end', 'Is_quarter_start',
              'Is_year_end', 'Is_year_start'):
        df[targ_pre + n] = getattr(fld.dt, n.lower())
    df[targ_pre + 'Elapsed'] = fld.astype(np.int64) // 10 ** 9
    if drop:
        df.drop(col, axis=1, inplace=True)












if __name__=="__main__":
    pass