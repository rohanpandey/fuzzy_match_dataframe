def fuzzymatching(df1,df2,column1_name,column2_name,n_top_items,type_match='simple'):
  import pandas as pd
  from fuzzywuzzy import fuzz
  from operator import itemgetter
  import json
  from fuzzywuzzy import process

  df1.columns=[element+'_1' for element in df1.columns]
  df2.columns=[element+'_2' for element in df2.columns]
  dataframe_final=pd.DataFrame()
  vals={}

  for index1,row1 in df1.iterrows():
    for index2,row2 in df2.iterrows():
      if type_match=='simple':
        vals[index2]=fuzz.ratio(row1[column1_name+'_1'],row2[column2_name+'_2'])
      elif type_match=='partial':
        vals[index2]=fuzz.partial_ratio(row1[column1_name+'_1'],row2[column2_name+'_2'])
      elif type_match=='token_sort':
        vals[index2]=fuzz.token_sort_ratio(row1[column1_name+'_1'],row2[column2_name+'_2'])
      elif type_match=='token_set':
        vals[index2]=fuzz.token_set_ratio(row1[column1_name+'_1'],row2[column2_name+'_2'])
    arr=sorted(vals.items(), key=itemgetter(1))[(0-n_top_items):]
    for i in reversed(arr):
      d1=(row1.to_dict())
      d2=(df2.iloc[i[0]].to_dict())
      d3={'Matching Score':i[1]}
      dataframe_final=dataframe_final.append({**d1,**d2,**d3},ignore_index=True)
  return dataframe_final