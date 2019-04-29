import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def match_name(item,item_list,min_score=0):
    max_score = -1
    # Returning empty name for no match as well
    max_name = ""
    # Iternating over all names in the other
    for i in item_list:
        #Finding fuzzy match score
        score = fuzz.ratio(item, i)
        # Checking if we are above our threshold and have a better score
        if (score > min_score) & (score > max_score):
            max_name = i
            max_score = score
    return (max_name, max_score)

data=pd.read_csv("test_cvs.csv")
master=data.dropna()
missing_name=data[data.names.isnull()]
for item in missing_name[['phone','address']].values.tolist():                                                                                  
     match=match_name(item,master[['phone','address']].values.tolist(),75)                                                                       
     print("name :",master.loc[master['phone']==match[0][0],'names'].tolist()[0],'score: ',match[1]) 
 
