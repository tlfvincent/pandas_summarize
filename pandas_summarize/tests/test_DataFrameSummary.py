import numpy as np
import pandas as pd
from unittest import TestCase
from pandas_summarize import DataFrameSummary


class TestDataFrameSummary(TestCase):
    def setUp(self):
        self.data = [[1, 'block', 1.4],
       		     [2, 'community', 6.0],
       		     [2, 'test', 5],
       		     [3, 'ok', 7.9],
       		     [None, '', 2.0]]
        self.df = pd.DataFrame(self.data, columns=['col1', 'col2', 'col3'])
        self.dfs = DataFrameSummary(self.df)
	
    def test_setup(self):
        assert isinstance(self.dfs, pd.DataFrame) is True

    def test_get_column_types(self):
        col_types_df = self.dfs.get_column_types()
        assert isinstance(col_types_df, pd.DataFrame) is True
        assert col_types_df.columns.tolist()  == ['column_name', 'value', 'variable']
	#assert col_types_df['value'].tolist() == [float64, O, float64]
