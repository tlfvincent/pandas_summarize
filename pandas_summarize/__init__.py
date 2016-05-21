from __future__ import division
from collections import Counter
import numpy as np
import pandas as pd

class DataFrameSummary(object):

    # define global variables
    TYPE_BOOL = 'bool'
    TYPE_NUMERIC = 'numeric'
    TYPE_DATE = 'date'
    TYPE_CATEGORICAL = 'categorical'
    TYPE_CONSTANT = 'constant'
    TYPE_UNIQUE = 'unique'


    def __init__(self, df):
        self.df = df
        self.columns = df.columns
        self.shape = df.shape
        self.count = df.count()
        self.columns_stats = self.get_summary()


    def get_column_types(self):
        '''get column type of each column in dataframe'''
        types = [[col, self.df[col].dtype] for col in self.columns]
        col_types_df = pd.DataFrame(types,
                                    columns=['column_name',
                                             'column_type'])
        return col_types_df


    def get_missing_count(self):
        '''get raw count of missing values in each column'''
        missing_cnt = [x, self.count[i]] for i, x in enumerate(self.columns)]
        missing_cnt_df = pd.DataFrame(missing_cnt,
                                      columns=['column_name',
                                               'missing_count'])
        return missing_cnt_df


    def get_missing_percentage(self):
        '''
        get proportion of missing values in each column of dataframe
        '''
        row_count = float(self.shape[0])
        missing_percent = [[x, self.count[i] / row_count] for i, x in enumerate(self.columns)]
        missing_percent_df = pd.DataFrame(missing_percent,
                                          columns=['column_name',
                                                   'missing_percent'])
        return missing_percent_df




