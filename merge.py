import pandas as pd
from fuzzywuzzy import fuzz


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

data=pd.read_csv("test_csv.csv")
master=data.dropna()
missing_name=data[data.names.isnull()]
dict_list=[]

# change as per field name and required
field_name="address"  # change as per field name
for item in missing_name[[field_name]].values.tolist():
    match=match_name(item,master[[field_name]].values.tolist(),75)
    #print("name :",master.loc[master[field_name]==match[0][0],'names'].tolist()[0],'score: ',match[1])

    # New dict for storing data
    dict_ = {}
    dict_.update({field_name:item[0]})
    dict_.update({"match_name": match[0][0]})
    dict_.update({"score": match[1]})
    dict_list.append(dict_)

merge_table = pd.DataFrame(dict_list)
# Display results
print(merge_table)