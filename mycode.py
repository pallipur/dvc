import pandas as pd
import os

#create a sample dataframe with column name

data = {"Name":['Alice','Bob','Charlie'],
        'Age':[25,30,45],
        'city':['NY',"LA","TN"]}

df=pd.DataFrame(data)



# CHANGE 01
new_row_loc={ 'Name':"Nilu",'Age':'33','city':'CA'}
df.loc[len(df.index)]=new_row_loc


#change 02
new_row_loc={ 'Name':"priyanka",'Age':'27','city':'MS'}
df.loc[len(df.index)]=new_row_loc



#create folder
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)


#save file in folder
file_path =os.path.join(data_dir,"sample_data.csv")
df.to_csv(file_path, index=False)

print("csv file saved to{file_path}")

