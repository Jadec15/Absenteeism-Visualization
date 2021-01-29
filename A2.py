#!/usr/bin/env python
# coding: utf-8

# In[69]:


#Jade Cabral Homework 2 due March 1st
import pandas as pd #using pandas library
import matplotlib.pyplot as plt#use line if using online version of jupyter notebook
source = "Absenteeism_at_work.xls"
data = pd.read_excel(source) #read in data
df = pd.DataFrame(data) #turn data into a data frame
df.head() #show a few rows to see that dataframe creation worked


# In[70]:


Age_table = pd.crosstab(index=df["Age"], columns="count") 
Age_table = (Age_table/Age_table.sum()) * 100
Age_table


# In[71]:


Transportation_table = pd.crosstab(index = df["Transportation expense"], columns="count")
Transportation_table = (Transportation_table/Transportation_table.sum()) * 100
Transportation_table


# In[72]:


Distance_table = pd.crosstab(index = df["Distance from Residence to Work"], columns="count")
Distance_table = (Distance_table/Distance_table.sum()) * 100
Distance_table


# In[73]:


plt.scatter(df["Transportation expense"], df["Distance from Residence to Work"], c = '#ab3230')
plt.title("Transportation expense by Distance from work")
plt.xlabel("Transportation expense")
plt.ylabel("Distsance from Work")
plt.show()


# In[74]:


plt.scatter(df["Age"], df["Transportation expense"], c = '#ff7f0e')
plt.title("Transportation expense by Age")
plt.xlabel("Age")
plt.ylabel("Transportation expense")
plt.show()


# In[75]:


plt.scatter(df["Age"], df["Distance from Residence to Work"], c = '#58a836')
plt.title("Distance from work by Age")
plt.xlabel("Age")
plt.ylabel("Distance from work")
plt.show()


# In[76]:


plt.hist(df["Transportation expense"], color = "#5a9629" )
plt.title("Transportation expense frequency")
plt.xlabel("Transportation expense")
plt.ylabel("Frequency")
plt.show()


# In[77]:


plt.hist(df["Age"], color = "#5fc1e8")
plt.title("Age frequency")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# In[78]:


plt.hist(df["Distance from Residence to Work"], color="#c24fab")
plt.title("Distance from Residence to Work frequency")
plt.xlabel("Distance from Residence to Work")
plt.ylabel("Frequency")
plt.show()


# In[79]:


df['Transportation expense'].value_counts().plot.bar(color = "#5a9629")
plt.title("Transportation Expense Frequency")
plt.xlabel("Distance from Residence to Work")
plt.ylabel("Frequency")
plt.show()


# In[80]:


df['Age'].value_counts().plot.bar(color = "#5fc1e8")
plt.title("Age Frequency")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# In[81]:


df['Distance from Residence to Work'].value_counts().plot.bar(color = "#c24fab")
plt.title("Distance from Residence to Work Frequency")
plt.xlabel("Distance from Residence to Work")
plt.ylabel("Frequency")
plt.show()


# In[82]:


plt.boxplot(df["Transportation expense"])
plt.title("Transportation expense data spread")
plt.xlabel("Box")
plt.ylabel("Transportation expense")
plt.show()


# In[83]:


plt.boxplot(df["Age"])
plt.title("Age data spread")
plt.xlabel("Box")
plt.ylabel("Age")
plt.show()


# In[84]:


plt.boxplot(df["Distance from Residence to Work"])
plt.title("Distance from Residence to Work Spread")
plt.xlabel("Box")
plt.ylabel("Distance from Residence to Work")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




