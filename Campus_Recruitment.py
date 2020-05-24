#!/usr/bin/env python
# coding: utf-8

# # Campus Recruitment

# Este conjunto de datos consta de datos de ubicación de estudiantes en un campus. Incluye porcentaje y especialización de secundaria y preparatoria. También incluye especialización de grado, tipo y experiencia laboral y ofertas salariales para los estudiantes colocados.

# * **si_no**	*Serial Number*
# 
# * **gender**	*Male='M',Female='F'*
# 
# * **ssc_p**	*Secondary School Certificate Board percentage- 1st-10th Grade*
# 
# * **ssc_b**	*Secondary School Certificate Board*
# 
# * **hsc_p**	*Higher Secondary Certificate Board percentage- 11th and 12th Grade*
# 
# * **hsc_b**	*Higher Secondary Certificate Board*
# 
# * **hsc_s**	*Specialization in Higher Secondary Education*
# 
# * **degree_p** *Degree Percentage*
# 
# * **degree_t** *Under Graduation(Degree type)- Field of degree education*
# 
# * **workex**	*Work Experience*
# 
# * **etest_p** *Porcentaje de prueba de empleabilidad (realizado por la universidad)*
# 
# * **specialisation** *Post Graduation(MBA)- Specialization*
# 
# * **mba_p**  *MBA percentage*
# 
# * **status** *Estado de la colocación: Colocado / No colocado*
# 
# * **salary** *Salario ofrecido por la empresa a los candidatos*

# Cosas que queremos determinar:
# * ¿Qué factor influyó en un candidato para ser colocado? 
# * ¿Importa el porcentaje para que uno sea colocado? 
# * ¿Qué especialización de grado es muy demandada por las empresas? 
# * Juega con los datos realizando todas las pruebas estadísticas.

# In[1]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('seaborn')
import seaborn as sns


# In[2]:


df = pd.read_csv('Placement_Data_Full_Class.csv')
print(df.columns.values)
df.head()


# In[3]:


# checking shape
print("The dataset has {} rows and {} columns.".format(*df.shape))

# ... and duplicates
print("It contains {} duplicates.".format(df.duplicated().sum()))


# In[4]:


total = df.isnull().sum().sort_values(ascending=False) #total de valores perdidos por columna ordenados 
#Porcentaje de valores perdidos respecto al total de cada columna
percent = ((df.isnull().sum())*100)/df.isnull().count().sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total','Percent'], sort=False).sort_values('Total', ascending=False)
missing_data.head(10)


# In[5]:


df.status.unique()


# In[6]:


df['status'].value_counts()


# Vamos a cambiar los valores NAN de la columna de *salary* por 0, ya que como vemos, coincide con las entradas de alumnos que no se les ha propocionado un trabajo.

# In[7]:


df['salary']=df['salary'].fillna(0)


# In[8]:


print("The dataset has {} rows and {} columns - after having dealt with missing values.".format(*df.shape))


# In[9]:


df.head()


# In[10]:


#Comprobamos que ya no tenemos NaNs en salary
pd.isnull(df['salary']).values.sum()


# ## Variables Dummie

# In[11]:


#Creamos función para que se haga automáticamente
def createDummies(df, var_name):
    dummy = pd.get_dummies(df[var_name], prefix=var_name)
    df = df.drop(var_name, axis = 1)
    df = pd.concat([df, dummy ], axis = 1)
    return df


# In[13]:


df2=createDummies(df, 'gender')
df2=createDummies(df, 'hsc_s')
df2=createDummies(df, 'ssc_b')
df2=createDummies(df, 'specialisation')
df2=createDummies(df, 'status')
df2=createDummies(df, 'degree_t')
df2.drop(['gender', 'hsc_s', 'ssc_b', 'specialisation','status'], axis=1, inplace=True)


# In[14]:


df2.head()


# In[ ]:




