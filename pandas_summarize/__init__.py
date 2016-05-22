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
        self.row_count = df.shape[0]
        self.count = df.count()


    def in_ipynb():
        '''
        check if code is running in ipython notebook or jupyter
        taken from SO thread:
        http://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook
        '''
        try:
            cfg = get_ipython().config 
            if cfg['IPKernelApp']['parent_appname'] == 'ipython-notebook':
                return True
            else:
                return False
        except NameError:
            return False


    def get_column_types(self):
        '''get column type of each column in dataframe'''
        types = [[col, self.df[col].dtype, 'dtypes'] for col in self.columns]
        col_types_df = pd.DataFrame(types,
                                    columns=['column_name',
                                             'value',
                                             'variable'])
        return col_types_df


    def get_unique_count(self):
        '''get number of unique values in each column'''
        unique_cnt = [[col,
                       self.df[col].nunique(),
                       'unique_count'] for col in self.columns]
        unique_cnt_df = pd.DataFrame(unique_cnt,
                                    columns=['column_name',
                                             'value',
                                             'variable'])
        return unique_cnt_df

    def get_missing_count(self):
        '''get raw count of missing values in each column'''
        missing_cnt = [[x,
                        self.row_count - self.count[i],
                        'missing_count'] for i, x in enumerate(self.columns)]
        missing_cnt_df = pd.DataFrame(missing_cnt,
                                      columns=['column_name',
                                               'value',
                                               'variable'])
        return missing_cnt_df


    def get_missing_percentage(self):
        '''get proportion of missing values in each column of dataframe'''
        missing_percent = [[x,
                           (self.count[i] / self.row_count)*100,
                           'missing_%'] for i, x in enumerate(self.columns)]
        missing_percent_df = pd.DataFrame(missing_percent,
                                          columns=['column_name',
                                                   'value',
                                                   'variable'])
        return missing_percent_df


    def get_summary(self):
        '''collect all column summaries and return as dataframe'''
        col_types_df = self.get_column_types()
        unique_cnt_df = self.get_unique_count()
        missing_cnt_df = self.get_missing_count()
        missing_percent_df = self.get_missing_percentage()
        df_summary = pd.concat([col_types_df,
                                unique_cnt_df,
                                missing_cnt_df,
                                missing_percent_df])
        df_summary = df_summary.pivot(index='variable',
                                      columns='column_name',
                                      values='value')
        df_summary.index.name = None
        return df_summary


    def get_distributions(self):
        '''generate distribution plots and summary statistics'''
        import matplotlib.pyplot as plt
        plt.style.use('fivethirtyeight')
        if in_ipynb:

        else:

        numeric_df = self.df._get_numeric_data()
        f = open('/home/jack/report.html','w')
        f.write(html_string)
        f.close()


