# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:10:10 2020

@author: Shruthi
"""

import matplotlib.pyplot as plt
import time
import pandas as pd
import seaborn as sns
import numpy ad np



data['Text']=data['Text'].str.lower()

"Replacing media into space so that easily can remove the rows"
data['Text'] = data['Text'].str.replace('<media omitted>','')
data['Text'] = data['Text'].str.replace('this message was deleted','')


data.index=range(l)

data['TW']=data['Text'].str.split().str.len()   #Provides total number of words in each row


data['TW'].replace(0, np.nan, inplace=True)# Replace 0 word row to nana value

data=data.dropna(subset=['TW','Date','Name','time','weekday']) # drop nan value row wise

total_word_file=dataset['TW'].sum() # total words in  file
dataset.isna().sum()




chater = data['Name'].value_counts().head(8).to_dict()

""" finding more """

Talker = data['Name'].value_counts().idxmax()
print("Frequent Talkative: ",Talker.upper())
result2.append(Talker)

Less_Talker = data['Name'].value_counts().idxmin()
print("Less talkative: ",Less_Talker.upper())
result2.append(Less_Talker)


Talker_chat = pd.DataFrame(data[data.Name == Talker])
Less_chat = pd.DataFrame(data[data.Name==Less_Talker])


unique_Frequency_Talker = pd.DataFrame(Talker_chat['text_wo_stop'].str.split(' ', expand=True).stack().value_counts())
unique_Frequency_Lesser = pd.DataFrame(Less_chat['text_wo_stop'].str.split(' ', expand=True).stack().value_counts())




unique_Frequency_Talker['Usage of word']=(unique_Frequency_Talker[0]/Talker_chat['text_wo_stop'].sum())*100
unique_Frequency_Lesser['Usage of word']=(unique_Frequency_Lesser[0]/Less_chat['text_wo_stop'].sum())*100  



solution_words = ['solution','contact','make','think','should','will','help',
                  'focus','i','would','compare','thought','check','error','anyone',
                  'apply','look','this','helpful','query','yes','using','pmcmd',
                  'domain','google','service','infomatica','user-name','work','perfectly','kill',
                  'dirctly','unix',]


try:
    
    Talker_Filter_list=pd.concat(Talker_Filter_list)#(obj.TalkerChecking(unique_Frequency_Talker,solution_words,Talker_Filter_list))
    result1.append(Talker_Filter_list)


except ValueError:
    print("Less Solution words by {}".format(Talker.upper()))
    
try:
    Talker_Filter_list.columns = ['Repeated_count','Frequency_Value']
    Talker_Filter_list['solution_Frequency']=(Talker_Filter_list['Repeated_count']/len(solution_words))*100
    Talker_out=Talker_Filter_list['solution_Frequency'].sum()/Talker_Filter_list.shape[0]
    print("solution Percentage of{}:".format(Talker.upper()), Talker_out,"%")     
    result1.append(Talker_out) 


except AttributeError:
    pass





def LesserChecking(self,unique_Frequrncy_Lesser, solution_words,Less_Filter_list):
    for i in solution_words:
        Less_Filter_list.append(unique_Frequency_Lesser[unique_Frequency_Lesser.index==i])
    print(Less_Talker,Less_Filter_list)


try:
    Less_Filter_list= pd.concat(Less_Filter_list)
    
    
except ValueError:
    print("No solution words by {}".format(Less_Talker.upper()))
    
return result2, result1
   
    
"""try:  
    Less_Filter_list.columns=['Repeated_count','Frequency_Value']
    Less_Filter_list['solution_Frequency']=(Less_Filter_list['Repeated_count']/len(solution_words))*100
    Less_out=Less_Filter_list['solution_Frequency'].sum()/Less_Filter_list.shape[0]
    print("Flirting Percentage of{}:".format(Less_Talker.upper()), Less_out,"%")

except AttributeError:
    pass











