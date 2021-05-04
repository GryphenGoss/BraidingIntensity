#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:40:21 2020

@author: gryphengoss
"""


import numpy as np
import pandas as pd
import os
import plotly.graph_objects as go
import plotly

os.chdir('/Users/gryphengoss/Desktop/Python_Plotting/')

Gdata = pd.read_excel('SK_dataC.xlsx', sheet_name = None)
S2017 = pd.read_excel('SK_dataC.xlsx', sheet_name = 'Slims_WettedXS_2017')

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

################################################## Down Stream Scatter Plots

ChanPlt = go.Figure()
Vgood = []
for key in one:
    Gdata[key] = Gdata[key].dropna()
    temp0 = np.array(Gdata[key]['Id'].value_counts())
    temp1 = np.array(Gdata[key]['Id'].value_counts().index.values)
    list0 = np.vstack((temp0,temp1))
    list0 = pd.DataFrame(list0.T)
    temp2 = np.array(namekey.loc[namekey[0] == key][1])
    temp2 = temp2[0]
    ChanPlt.add_trace(go.Scatter(x=list0[1], y=list0[0],
                    mode='markers',
                    name= temp2))
    ChanPlt.update_layout(
    title="",
    xaxis_title="Distance Downstream (m)",
    yaxis_title="Number of Wetted Channels",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="black"
    ))
    
plotly.offline.plot(ChanPlt)   
#ChanPlt.write_html('ChanPlt.html')

################################################## Down Stream: Lengths
ChanPltLen = go.Figure()
VVgood = []
for key in one:
    Gdata[key] = Gdata[key].dropna()
    temp00 = np.array(Gdata[key]['Length_m'].value_counts())
    temp11 = np.array(Gdata[key]['Id'].value_counts().index.values)
    list00 = np.vstack((temp00,temp11))
    list00 = pd.DataFrame(list00.T)
    temp22 = np.array(namekey.loc[namekey[0] == key][1])
    temp22 = temp22[0]
    ChanPltLen.add_trace(go.Scatter(x=list00[1], y=list00[0],
                    mode='markers',
                    name= temp22))
    ChanPltLen.update_layout(
    title="Sum of all lengths downstream",
    xaxis_title="Distance Downstream (m)",
    yaxis_title="Active Channel Widths",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="black"
    ))
    
plotly.offline.plot(ChanPltLen)   
#ChanPlt.write_html('ChanPlt.html')







##################################################Box Plots - Slims Feb 8

import plotly.graph_objects as go
import plotly

Slimsbox = go.Figure()


Slimsbox.add_trace(go.Box(
    y=Slims['BI'],
    x=Slims['Year'],
    name='Slims',
    marker_color='black',
    fillcolor='white',
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

ArithmeticError(args)Slimsbox.update_layout(
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

################################################## Kaskawulsh Box plot Feb 8

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





######################################### Kaskawulsh Braiding intensity

#Slimsbox.write_image('Slims.svg')

################################################## Yearly Scatter Plots


#Kaskbox.write_image('Kask.svg') 


################################ Downstream plot 12/15/2020

BItable2 = pd.DataFrame(Gresults, columns = ['BI','Date','River Year','Id'])     

BItable2['Date'] = pd.to_datetime(BItable2['Date'])
BItable2['Month'] = BItable2['Date'].dt.month
BItable2['River'] = BItable2['River Year'].str.contains('Kask')
BItable2['River'] = BItable2['River'].replace(to_replace= True, value='Kask')
BItable2['River'] = BItable2['River'].replace(to_replace= False, value='Slims')

SlimsJuly = BItable2[BItable2['River'] == 'Slims']
KaskJuly = BItable2[BItable2['River'] == 'Kask']


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


ChanPlt2 = go.Figure()
Vgood2 = []
for key in one:
    Gdata[key] = Gdata[key].dropna()
    temp0 = np.array(Gdata[key]['Id'][Gdata[key]['Date'].dt.month == 7].value_counts())
    temp10 = len(Gdata[key]['Date'][Gdata[key]['Date'].dt.month == 7].value_counts().index)
    temp20 = temp0/temp10
    temp1 = np.array(Gdata[key]['Id'][Gdata[key]['Date'].dt.month == 7].value_counts().index.values)
    list0 = np.vstack((temp20,temp1))
    list0 = pd.DataFrame(list0.T)
    temp2 = np.array(namekey.loc[namekey[0] == key][1])
    temp2 = temp2[0]
    ChanPlt2.add_trace(go.Scatter(x=list0[1], y=list0[0],
                    mode='markers',
                    name= temp2))
    ChanPlt2.update_layout(
    title="",
    xaxis_title="Distance Downstream (m)",
    yaxis_title="Number of Wetted Channels",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="black"
    ))
    
plotly.offline.plot(ChanPlt2)   
ChanPlt2.write_html('ChanPlt2.html')












