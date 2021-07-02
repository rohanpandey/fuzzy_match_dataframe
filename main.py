from fuzzy_match import fuzzymatching
import pandas as pd

if __name__ == '__main__':
    df1=pd.read_excel("./names.xlsx")
    df2=pd.read_excel("./names.xlsx")
    column1_name='Names'
    column2_name='Names'
    n_top_items=5
    
    print(fuzzymatching(df1,df2,column1_name,column2_name,n_top_items))