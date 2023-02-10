#!/usr/bin/env python
# coding: utf-8

# In[147]:

import pandas as pd
import numpy as np
import statistics as stats


# In[148]:

a=[1,2,3,4...


# In[149]:


type(a)


# In[150]:

a=np.array(a)


# In[151]:


a


# In[152]:


b=np.random.randint(1,14,size=(3,6))


# In[153]:


b


# In[154]:


df=pd.DataFrame(b,columns=['a','b','c','d','e','f'],index=['x','y','z'])


# In[155]:


df.shape


# In[156]:


df


# In[157]:


df['b']


# In[158]:


d=np.random.randint(5,10,size=(3,6))


# In[159]:


d


# In[160]:


df1=pd.DataFrame(d,columns=['a','b','c','d','e','f'],index=['u','v','w'])


# In[161]:


df1.shape


# In[162]:


df1


# In[163]:


df3=pd.concat([df,df1])


# In[164]:


df3.shape


# df3

# In[165]:


df3


# In[166]:


df3.loc[['x','z'],['a','b','c']]


# In[167]:


dfT = pd.read_csv('employee.csv')


# In[168]:


dfT.head()


# In[169]:


dfT.shape


# In[170]:


dfT.isnull().sum()


# In[171]:


dfT.drop('QUINN/EDUCATION INCENTIVE',axis=1,inplace=True)


# In[172]:


dfT.drop('DETAIL',axis=1,inplace=True)


# In[173]:


dfT.drop('INJURED',axis=1,inplace=True)


# In[174]:


dfT.drop('RETRO',axis=1,inplace=True)


# In[175]:


dfT.drop('OVERTIME',axis=1,inplace=True)


# In[176]:


dfT.drop('Unnamed: 1',axis=1,inplace=True)


# In[177]:


dfT.drop('OTHER',axis=1,inplace=True)


# In[178]:


dfT.isnull().sum()


# In[179]:


dfT.head()


# In[180]:


dfT['REGULAR']=dfT['REGULAR'].str.replace(',','')


# In[181]:


dfT['REGULAR']=dfT['REGULAR'].str.replace('$','')


# In[182]:


dfT.head()


# In[183]:


dfT['TOTAL EARNINGS']=dfT['TOTAL EARNINGS'].str.replace('$','')


# In[184]:


dfT['TOTAL EARNINGS']=dfT['TOTAL EARNINGS'].str.replace(',','')


# In[185]:


dfT.head()


# In[186]:


dfT.info()


# In[187]:


dfT['REGULAR']=dfT['REGULAR'].astype('float',inplace=True)


# In[188]:


dfT.info()


# In[189]:


dfT['TOTAL EARNINGS']=dfT['TOTAL EARNINGS'].astype('float',inplace=True)


# In[190]:


dfT.info()


# In[191]:


dfT.isnull().sum()


# In[192]:


dfT['Postal']=dfT['POSTAL'].str.extract('([0-9]+)')


# In[193]:


dfT.info()


# In[194]:


dfT.head()


# In[195]:


dfT.drop('POSTAL',axis=1,inplace=True)


# In[196]:


dfT.info()


# In[197]:


dfT['Postal'].fillna(method='ffill',inplace=True)


# In[198]:


dfT.info()


# In[199]:


dfT.isnull().sum()


# In[200]:


dfT.isnull().sum()


# In[201]:


dfT.info()


# In[202]:


dfT['Postal']=dfT['Postal'].astype('int',inplace=True)


# In[203]:


dfT.info()


# In[204]:


dfT['REGULAR']=dfT['REGULAR'].fillna(dfT.groupby(['DEPARTMENT_NAME','TITLE'])['REGULAR'].transform('mean'))


# In[205]:


dfT.info()


# In[206]:


dfT['Title']=dfT['TITLE'].str.extract('([a-zA-Z ]+[a-z/A-Z' '()]*)')


# In[207]:


dfT.head(70)


# In[208]:


dfG = pd.DataFrame({'key':['A','B','C','A','B','C'], 'Data1': range(6),'Data2'
:np.random.randint(0,10,6)})


# In[209]:


dfG


# In[210]:


dfG.groupby('key').aggregate(np.mean)


# In[211]:


dfG.groupby('key').sum()


# In[212]:


dfT.head()


# In[213]:


def find_boundaries(df, variable, distance):
 lower_boundary=df[variable].mean()-(df[variable].std()*distance)
 upper_boundary=df[variable].mean()+(df[variable].std()*distance)
 return upper_boundary, lower_boundary


# In[214]:


RM_upper_limit, RM_lower_limit = find_boundaries(dfT,'Postal',1.5)


# In[215]:


RM_upper_limit, RM_lower_limit


# In[216]:


import seaborn as sns


# In[239]:


sns.boxplot(dfT['Postal'],whis=1.5)


# In[218]:


outliers = np.where(dfT['Postal'] > RM_upper_limit, True, np.where(dfT['Postal'] < RM_lower_limit, True,False))


# In[219]:


outliers.shape


# In[220]:


outliers


# In[221]:


boston_trimmed = dfT.loc[~(outliers)]


# In[222]:


boston_trimmed.shape


# In[223]:


boston_trimmed.head()


# In[224]:


sns.boxplot(boston_trimmed['Postal'],whis=1.5)


# In[225]:


RM_upper_limit, RM_lower_limit = find_boundaries(dfT,'TOTAL EARNINGS',2)


# In[226]:


RM_upper_limit, RM_lower_limit


# In[227]:


sns.boxplot(dfT['TOTAL EARNINGS'],whis=1.5)


# In[228]:


outliers = np.where(dfT['TOTAL EARNINGS'] > RM_upper_limit, True, np.where(dfT['TOTAL EARNINGS'] < RM_lower_limit, True,False))


# In[229]:


trimmed = dfT.loc[~(outliers)]


# In[230]:


trimmed.shape


# In[231]:


sns.boxplot(trimmed['TOTAL EARNINGS'],whis=1.5)


# In[232]:


RM_upper_limit, RM_lower_limit = find_boundaries(dfT,'REGULAR',1.5)


# In[233]:


RM_upper_limit, RM_lower_limit


# In[234]:


sns.boxplot(dfT['REGULAR'],whis=1.5)


# In[235]:


outliers = np.where(dfT['REGULAR'] > RM_upper_limit, True, np.where(dfT['REGULAR'] < RM_lower_limit, True,False))


# In[236]:


trimmed = dfT.loc[~(outliers)]


# In[237]:


sns.boxplot(trimmed['REGULAR'],whis=1.5)


# In[83]:


rng_hr = pd.date_range('2019-03-05', periods=20, freq='H')
rng_month = pd.date_range('2019-03-05', periods=20, freq='M')
df = pd.DataFrame({'date1': rng_hr, 'date2': rng_month})
df.head()


# In[84]:


df['elapsed_days'] = (df['date2'] - df['date1']).dt.days
df.head()


# In[86]:


df['months_passed'] = ((df['date2'] - df['date1'])/ np.timedelta64(1, 'M'))
df['months_passed']=np.round(df['months_passed'],0)
df.head()


# In[ ]:


RM_upper_limit, RM_lower_limit = find_boundaries(dfT,'TOTAL EARNINGS',2)
RM_upper_limit, RM_lower_limit
sns.boxplot(dfT['TOTAL EARNINGS'],whis=2)
outliers = np.where(dfT['TOTAL EARNINGS'] > RM_upper_limit, True, np.where(dfT['TOTAL EARNINGS'] < RM_lower_limit, True,False))
trimmed = dfT.loc[~(outliers)]
sns.boxplot(trimmed['TOTAL EARNINGS'],whis=3)

