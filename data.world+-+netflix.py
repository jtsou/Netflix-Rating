
# coding: utf-8

# In[74]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')

df = pd.read_excel(r"C:\Users\jenni\Box Sync\Dataset\netflix.xlsx")

#to see snipet of the code
df.head()



#Provide overview of the rating
df.groupby(['rating']).describe()


#Show what each rating stands for
df[['rating','ratingLevel']].drop_duplicates()

df.groupby(['rating']).count()


#netflix show by rating
df[['rating', 'release year']].groupby('release year').describe()#['release year'].describe()



#plot
fig, ax = plt.subplots()
fig.set_size_inches(16, 12)
sns.barplot(x='release year', y ='user rating score', hue='rating', data=df)
plt.grid()
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)





