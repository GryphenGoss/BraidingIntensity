#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:57:45 2021

@author: gryphengoss
"""



import numpy as np
import pandas as pd
import os
import plotly.graph_objects as go
import plotly

os.chdir('/Users/gryphengoss/Desktop/Python_Plotting/')

Gdata = pd.read_excel('SK_dataCC.xlsx', sheet_name = None)
S2017 = pd.read_excel('SK_dataCC.xlsx', sheet_name = 'Slims_WettedXS_2017')

for key in Gdata:
    if np.any(Gdata[key].columns == 'date'):
        Gdata[key]['Date'] = pd.to_datetime(Gdata[key]['date'], format="%m/%d/%Y")
    else:
        Gdata[key]['Date'] = pd.to_datetime(Gdata[key]['Date'], format="m/%d/%Y") 

#Calculate braiding intensity
Gresults = []
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
BItable = pd.DataFrame(Gresults, columns = ['BI','Date','River Year','Id'])             
        
BItable['Date'] = pd.to_datetime(BItable['Date'])
BItable['Year'] = BItable['Date'].dt.year
BItable['River'] = BItable['River Year'].str.contains('Kask')
BItable['River'] = BItable['River'].replace(to_replace= True, value='Kask')
BItable['River'] = BItable['River'].replace(to_replace= False, value='Slims')

Slims = BItable[BItable['River'] == 'Slims']
Kask = BItable[BItable['River'] == 'Kask']


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


########################## Plotting peak melt season braiding intensity: July/A
