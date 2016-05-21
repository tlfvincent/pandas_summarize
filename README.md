# pandas_summarize
An extension to the Pandas library to comprehensively summarize dataframes

```
import pandas as pd
from df_summary import DataFrameSummary

# define example DataFrame
lst = [[1, 'block', 1.4],
       [2, 'community', 6.0],
       [2, 'test', 5],
       [3, 'ok', 7.9],
       [None, '', 2.0]]
df = pd.DataFrame(lst, columns=['col1', 'col2', 'col3'])
```

```
dfs = DataFrameSummary(df)
dfs.get_summary()
```

```
column_name       col1    col2     col3
dtypes         float64  object  float64
missing_%           80     100      100
missing_count        1       0        0
```