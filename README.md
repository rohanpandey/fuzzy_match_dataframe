# fuzzy_match_dataframe

Calculate the similarity (Levenshtein distance) between two columns in two dataframes. 
For each item in the column1 (dataframe1), returns the top matches (n) that have the highest similarity in column2 (dataframe2).

##Installation

```bash
pip install -r requirements.txt
```

## Usage
1. Sample shown in main.py
2. Function usage:

```bash
fuzzymatching(df1,df2,column1_name,column2_name,n_top_items,type_match='simple')
``` 
Here:
df1 - Pandas Dataframe1
df2 - Pandas Dataframe2
column1_name - Name of column1 in df1 that requires matching.
column2_name - Name of column2 in df2 that needs to be matched with column1.
n_top_items - Number of matching items to be returned with the highest score.
type_match - Options: 'simple','partial_ratio','token_sort_ratio','token_set_ratio'

### References

[1] https://github.com/seatgeek/fuzzywuzzy