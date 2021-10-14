import pandas as pd
import re
import numpy as np
import json
import types
import random

def pd_check_col_str(df, colname, regex_str):
    if df[colname].apply(lambda x:isinstance(x, list)).any(0):
        return df[colname].apply(lambda x:regex_str in x).fillna(False)
    else:
        return df[colname].str.contains(regex_str, case=False).fillna(False)
        
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
