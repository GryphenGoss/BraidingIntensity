#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import plotly.graph_objects as go
import plotly


# In[2]:


os.chdir('/Users/gryphengoss/Desktop/Python_Plotting/')


# In[3]:


Gdata = pd.read_excel('SK_dataC.xlsx', sheet_name = None)

for key in Gdata:
    if np.any(Gdata[key].columns == 'date'):
        Gdata[key]['Date'] = pd.to_datetime(Gdata[key]['date'], format="%m/%d/%Y")
    else:
        Gdata[key]['Date'] = pd.to_datetime(Gdata[key]['Date'], format="m/%d/%Y") 


# In[4]:


Gresults = []


# In[5]:


for key in Gdata:
    Gdata[key] = Gdata[key].dropna()
    for UDay in Gdata[key]['Date'].dt.date.unique():
        temp0 = UDay.strftime('%m/%d/%Y')
        templist = Gdata[key][(Gdata[key]['Date'] == temp0)] 
        temp1 = len(templist)
        temp2 = len(templist['Id'].unique())
        temp3 = temp1/temp2 
        temp4 = templist['Id'].unique()
        Gresults.append([temp3, temp0, key, temp4])
        Gresults   


# In[ ]:





# In[6]:


BItable = pd.DataFrame(Gresults, columns = ['BI','Date','River Year','Id'])     


# In[ ]:





# In[7]:


BItable['Date'] = pd.to_datetime(BItable['Date'])


# In[ ]:





# In[8]:


BItable['Year'] = BItable['Date'].dt.year


# In[9]:


BItable['River'] = BItable['River Year'].str.contains('Kask')


# In[10]:


BItable['River'] = BItable['River'].replace(to_replace= True, value='Kask')


# In[11]:


BItable['River'] = BItable['River'].replace(to_replace= False, value='Slims')


# In[ ]:





# In[12]:


Slims = BItable[BItable['River'] == 'Slims']


# In[13]:


Kask = BItable[BItable['River'] == 'Kask']


# In[14]:


Slims.to_csv('/Users/gryphengoss/Desktop/Slims.csv')


# In[15]:


#Kask.to_csv('/Users/gryphengoss/Desktop/Kask.csv')


# In[16]:


#Calcaulte Number of Channels 
#Number of wet cross-sections versus distance
Counts = pd.DataFrame(columns = ['Kask_WettedXS_2020', 'Kask_WettedXS_2019',
                                 'Kask_WettedXS_2018','Kask_WettedXS_2017',
                                 'Kask_WettedXS_2016','Kask_WettedXS_2015',
                                 'Kask_WettedXS_2014','Kask_WettedXS_2013',
                                 'Slims_WettedXS_2020','Slims_WettedXS_2019',
                                 'Slims_WettedXS_2018','Slims_WettedXS_2017',
                                 'Slims_WettedXS_2016','Slims_WettedXS_2015',
                                 'Slims_WettedXS_2014','Slims_WettedXS_2013'], dtype=('float64'))
for key in Gdata:
    Gdata[key] = Gdata[key].dropna()
    temp0 = Gdata[key]['Id'].value_counts()
    Counts[key] = temp0

Counts = Counts.fillna(0)

two = np.array(['Kaskawulsh 2020', 'Kaskawulsh 2019',
         'Kaskawulsh 2018','Kaskawulsh 2017',
         'Kaskawulsh 2016','Kaskawulsh 2015',
         'Kaskawulsh 2014','Kaskawulsh 2013',
         'Ä’äy Chù 2020','Ä’äy Chù 2019',
         'Ä’äy Chù 2018','Ä’äy Chù 2017',
         'Ä’äy Chù 2016','Ä’äy Chù 2015',
         'Ä’äy Chù 2014','Ä’äy Chù 2013'])

one = np.array(['Kask_WettedXS_2020', 'Kask_WettedXS_2019',
                                 'Kask_WettedXS_2018','Kask_WettedXS_2017',
                                 'Kask_WettedXS_2016','Kask_WettedXS_2015',
                                 'Kask_WettedXS_2014','Kask_WettedXS_2013',
                                 'Slims_WettedXS_2020','Slims_WettedXS_2019',
                                 'Slims_WettedXS_2018','Slims_WettedXS_2017',
                                 'Slims_WettedXS_2016','Slims_WettedXS_2015',
                                 'Slims_WettedXS_2014','Slims_WettedXS_2013'])
one = pd.Series(one)
two = pd.Series(two)
namekey = pd.concat([one, two], axis = 1)


# In[17]:


import plotly.graph_objects as go
import plotly

Slimsbox = go.Figure()


Slimsbox.add_trace(go.Box(
    y=Slims['BI'],
    x=Slims['Year'],
    name='Slims',
    marker_color='black',
    fillcolor='white',
    boxpoints=False,
    quartilemethod="inclusive"
))

Slimsbox.update_layout(
    title="",
    xaxis_title="Years",
    yaxis_title="",
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        family="Arial",
        color="black",
        size=30
    )
)

Slimsbox.update_layout(
    yaxis = dict(
        range = [0, 7],
        tickmode = 'array',
        tickvals = [1, 2, 3, 4, 5, 6,7],
        zerolinecolor='black',
        gridcolor='white',
        ticktext = ['1', '2', '3', '4', '5','6','7']
    )   
)

Slimsbox.update_layout(
    xaxis = dict(
        #range = [0, 9],
        #tickmode = 'array',
        #tickvals = [0,1, 2, 3, 4, 5, 6, 7, 8],
        zerolinecolor='black',
        gridcolor='white',
        #ticktext = ['0','2013', '2014', '2015', '2016', '2017','2018','2019','2020'],
    )   
)
Slimsbox.write_image("SlimsBI.svg")
plotly.offline.plot(Slimsbox)


# In[ ]:


import plotly.graph_objects as go
import plotly

Kaskbox = go.Figure()

Kaskbox.add_trace(go.Box(
    y=Kask['BI'],
    x=Kask['Year'],
    name='Kask',
    marker_color='black',
    fillcolor='white',
))

Kaskbox.update_layout(
    title="",
    xaxis_title="Years",
    yaxis_title="",
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        family="Arial",
        color="black",
        size=30
    )
)

Kaskbox.update_layout(
    yaxis = dict(
        range = [0, 7],
        tickmode = 'array',
        tickvals = [1, 2, 3, 4, 5, 6,7],
        zerolinecolor='black',
        gridcolor='white',
        ticktext = ['1', '2', '3', '4', '5','6','7']
    )   
)

Kaskbox.update_layout(
    xaxis = dict(
        #range = [0, 9],
        #tickmode = 'array',
        #tickvals = [0,1, 2, 3, 4, 5, 6, 7, 8],
        zerolinecolor='black',
        gridcolor='white',
        #ticktext = ['0','2013', '2014', '2015', '2016', '2017','2018','2019','2020'],
    )   
)
Kaskbox.write_image("KaskBI.svg")
plotly.offline.plot(Kaskbox)


# In[ ]:




