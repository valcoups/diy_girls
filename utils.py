import pandas as pd
import re
import numpy as np
import json
import types
import random
from ast import literal_eval
from collections import Iterable, Counter

def print_df_column_names(df):

    for i, column_name in enumerate(df.columns):
      print(f'{i+1:>3}. {column_name}')

def check_df_col_str(df, colname, regex_str):

    return df[colname].str.contains(regex_str, case=False).fillna(False)
        
def normalize_text(text):
    text = text.lower()
    text = text.translate({ord(ch):'' for ch in """"()[]-'./\&"""})
    text = '_'.join(text.split())
    return text
    
def find_titles_by_feature(data, feature_column, feature_query):

    feature_str = normalize_text(feature_query)
    subset = data.loc[check_df_col_str(data, feature_column, feature_str)]
    
    if subset.empty:
        print('No titles matched the query!')
    
    return subset
    
def get_list_of_features(*items, delims=None):
    """
    Yield items from any nested iterable and protecting strings
    """

    if delims is not None:
        regex = '|'.join(map(re.escape, delims))
        split = lambda str_x:[str_x.strip() for str_x in re.split(regex, str_x, maxsplit=0) if str_x.strip()]
    else:
        regex = None
        split = lambda str_x:[str_x]

    def flatten(items):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, (str, bytes, dict)):
                for sub_x in flatten(x):
                    yield sub_x
            else:
                if isinstance(x, (str, bytes)):
                    for sub_x in split(x):
                        yield sub_x

                else:
                    if x not in [np.nan, None, '']:
                        yield x

    lst = list(flatten(items))

    return lst



