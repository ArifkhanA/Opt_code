#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import packages

import numpy as np
import pandas as pd
from datetime import date

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)

filename="727"


# In[2]:


#Input and Output Path setting

input_path = "/Users/condenast/Desktop/opt_files/inputfile/"+str(filename)+".xlsx"

output_path = "/Users/condenast/Desktop/opt_files/outputfile/Op_"+str(filename)+".xlsx"


# In[3]:


#Input path

optfile=pd.read_excel(input_path)
optfile.shape


# In[4]:


#Data filterations

optfile['Estimated Cost Per Ticket LNR']= optfile['Estimated Cost Per Ticket LNR'].replace('[\$,]', '', regex=True).astype(float)

x1 = date.today()

today=x1.strftime('%-m/%-d/%Y')

x=optfile["CTR"]<"1.00%"

y=optfile["Estimated Tickets Sold LNR"]=="0" 

z=optfile["Estimated Cost Per Ticket LNR"]>12.00

ti=pd.concat([optfile[x], optfile[y], optfile[z]]).drop_duplicates()

st= ti[(ti["Campaign Start Time (Dimension)"] != today) & (ti["Campaign Stop Time (Dimension)"]!=today)]


# In[5]:


#Output path

st.sort_values(by=['Campaign Stop Time (Dimension)','Campaign']).to_excel(output_path,index=False)

st.shape


# In[ ]:




