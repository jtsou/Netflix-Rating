
# coding: utf-8

# In[74]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# In[59]:

df = pd.read_excel(r"C:\Users\jenni\Box Sync\Dataset\netflix.xlsx")


# In[60]:

df.head(1)


# In[61]:

#Provide overview of the rating

df.groupby(['rating']).describe()


# In[62]:

#Show what each rating stands for
df[['rating','ratingLevel']].drop_duplicates()


# In[72]:

df.groupby(['rating']).count()


# In[63]:

#netflix show by rating
df[['rating', 'release year']].groupby('release year').describe()#['release year'].describe()


# In[88]:

#set size for the plot
fig, ax = plt.subplots()
fig.set_size_inches(16, 12)
sns.barplot(x='release year', y ='user rating score', hue='rating', data=df)
plt.grid()
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[ ]:



