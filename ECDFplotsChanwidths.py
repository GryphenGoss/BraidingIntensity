#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 16:54:58 2021

@author: gryphengoss
"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import seaborn as sns

file="/Users/gryphengoss/Desktop/Python_Plotting/GlaciersUnzipped.xls"

#Load spreadsheet
x1 = pd.ExcelFile(file)

#Print the sheet names
#print(x1.sheet_names)
#Load a sheet into a dataframe by name of: df1
df1 = x1.parse("KlinaCCIdata1949")
df2 = x1.parse("KlinaCCIdata2020")
df3 = x1.parse("HalloCCIdata1951")
df4 = x1.parse("HalloCCIdata2020")
df5 = x1.parse("SlimsCCIdata1950")
df6 = x1.parse("SlimsCCIdata2015")
df7 = x1.parse("MeadeCCIdata1979")
df8 = x1.parse("MeadeCCIdata2020")
df9 = x1.parse("RobertCCIdata1954")
df10 = x1.parse("RobertCCIdata2020")
df11 = x1.parse("SusitnaCCIdata1949")
df12 = x1.parse("SusitnaCCIdata2020")
df13 = x1.parse("KaskCCIdata1950")
df14 = x1.parse("KaskCCIdata2015")
df15 = x1.parse("JuneauCCIdata1958")
df16 = x1.parse("JuneauCCIdata2020")
df17 = x1.parse("LillooetCCIdata1951")
df18 = x1.parse("LillooetCCIdata2020")
df19 = x1.parse("ActRobsCCIdata1978")
df20 = x1.parse("ActRobsCCIdata2020")
df21 = x1.parse("KukakCCIdata1951")
df22 = x1.parse("KukakCCIdata2020")


#Klinaklini
x = df1['Length']
y = df2['Length']

#Hallo
a = df3['Length']
b = df4['Length']

#Slims
c = df5['Length']
d = df6['Length']


#Meade
e = df7['Length']
f = df8['Length']


#NWRobs
g = df9['Length']
h = df10['Length']


#Susitna
i = df11['Length']
j = df12['Length']


#Kask
k = df13['Length']
l = df14['Length']


#Tulsequah
m = df15['Length']
n = df16['Length']

#Lillooet
o = df17['Length']
p = df18['Length']

#ActRobs
q = df19['Length']
r = df20['Length']


#KukakBay
s = df21['Length']
t = df22['Length']



sns.set(font_scale=2)
sns.set_style("white")
sns.set_style("ticks")

#sns.set(rc={'axes.facecolor':'white', 'figure.facecolor':'white'})

fig, ax = plt.subplots(6,2,sharex=False, figsize=(13,15))
ax[-1, -1].axis('off')

#column 1
sns.ecdfplot(data=df1, x=x, ax=ax[0,0], stat = "proportion", hue = None)
sns.ecdfplot(data=df2, x=y, ax=ax[0,0], stat = "proportion")
ax[0,0].set_xlim([0, 200])
ax[0,0].set_ylabel("")
ax[0,0].set_xlabel("")
ax[0,0].yaxis.set_ticklabels([])


sns.ecdfplot(data=df3, x=a, ax=ax[1,0], stat = "proportion")
sns.ecdfplot(data=df4, x=b, ax=ax[1,0], stat = "proportion")
ax[1,0].set_xlim([0, 60])
ax[1,0].set_ylabel("")
ax[1,0].set_xlabel("")
ax[1,0].yaxis.set_ticklabels([])

sns.ecdfplot(data=df5, x=c, ax=ax[2,0], stat = "proportion")
sns.ecdfplot(data=df6, x=d, ax=ax[2,0], stat = "proportion")
ax[2,0].set_xlim([0, 125])
ax[2,0].set_ylabel("")
ax[2,0].set_xlabel("")
ax[2,0].yaxis.set_ticklabels([])

sns.ecdfplot(data=df7, x=e, ax=ax[3,0], stat = "proportion")
sns.ecdfplot(data=df8, x=f, ax=ax[3,0], stat = "proportion")
ax[3,0].set_xlim([0, 150])
ax[3,0].set_ylabel("")
ax[3,0].set_xlabel("")
ax[3,0].yaxis.set_ticklabels([])

sns.ecdfplot(data=df9, x=g, ax=ax[4,0], stat = "proportion")
sns.ecdfplot(data=df10, x=h, ax=ax[4,0], stat = "proportion")
ax[4,0].set_xlim([0, 60])
ax[4,0].set_ylabel("")
ax[4,0].set_xlabel("")
ax[4,0].yaxis.set_ticklabels([])


sns.ecdfplot(data=df11, x=i, ax=ax[5,0], stat = "proportion")
sns.ecdfplot(data=df12, x=j, ax=ax[5,0], stat = "proportion")
ax[5,0].set_xlim([0, 60])



#Column 2

sns.ecdfplot(data=df13, x=k, ax=ax[0,1], stat = "proportion")
sns.ecdfplot(data=df14, x=l, ax=ax[0,1], stat = "proportion")
ax[0,1].set_xlim([0, 60])
ax[0,1].set_ylabel("")
ax[0,1].set_xlabel("")
ax[0,1].yaxis.set_ticklabels([])

sns.ecdfplot(data=df15, x=m, ax=ax[1,1], stat = "proportion")
sns.ecdfplot(data=df16, x=n, ax=ax[1,1], stat = "proportion")
ax[1,1].set_xlim([0, 200])
ax[1,1].set_ylabel("")
ax[1,1].set_xlabel("")
ax[1,1].yaxis.set_ticklabels([])

sns.ecdfplot(data=df17, x=o, ax=ax[2,1], stat = "proportion")
sns.ecdfplot(data=df18, x=p, ax=ax[2,1], stat = "proportion")
ax[2,1].set_xlim([0, 75])
ax[2,1].set_ylabel("")
ax[2,1].set_xlabel("")
ax[2,1].yaxis.set_ticklabels([])

sns.ecdfplot(data=df19, x=q, ax=ax[3,1], stat = "proportion")
sns.ecdfplot(data=df20, x=r, ax=ax[3,1], stat = "proportion")
ax[3,1].set_xlim([0, 80])
ax[3,1].set_ylabel("")
ax[3,1].set_xlabel("")
ax[3,1].yaxis.set_ticklabels([])

sns.ecdfplot(data=df21, x=s, ax=ax[4,1], stat = "proportion")
sns.ecdfplot(data=df22, x=t, ax=ax[4,1], stat = "proportion")
ax[4,1].set_xlim([0, 50])
ax[4,1].set_ylabel("")
ax[4,1].yaxis.set_ticklabels([])



fig.tight_layout(pad=0.5)
plt.savefig("PorpEcdf.svg", format="svg")



#### COUNT VERSION

sns.set(font_scale=2)
sns.set_style("white")
sns.set_style("ticks")

#sns.set(rc={'axes.facecolor':'white', 'figure.facecolor':'white'})

fig, ax = plt.subplots(6,2,sharex=False, figsize=(13,15))
ax[-1, -1].axis('off')

#column 1
sns.ecdfplot(data=df1, x=x, ax=ax[0,0], stat = "count", hue = None)
sns.ecdfplot(data=df2, x=y, ax=ax[0,0], stat = "count")
ax[0,0].set_xlim([0, 200])
ax[0,0].set_ylabel("")
ax[0,0].set_xlabel("")
#ax[0,0].yaxis.set_ticklabels([])


sns.ecdfplot(data=df3, x=a, ax=ax[1,0], stat = "count")
sns.ecdfplot(data=df4, x=b, ax=ax[1,0], stat = "count")
ax[1,0].set_xlim([0, 60])
ax[1,0].set_ylabel("")
ax[1,0].set_xlabel("")
#ax[1,0].yaxis.set_ticklabels([])

sns.ecdfplot(data=df5, x=c, ax=ax[2,0], stat = "count")
sns.ecdfplot(data=df6, x=d, ax=ax[2,0], stat = "count")
ax[2,0].set_xlim([0, 125])
ax[2,0].set_ylabel("")
ax[2,0].set_xlabel("")
#ax[2,0].yaxis.set_ticklabels([])

sns.ecdfplot(data=df7, x=e, ax=ax[3,0], stat = "count")
sns.ecdfplot(data=df8, x=f, ax=ax[3,0], stat = "count")
ax[3,0].set_xlim([0, 150])
ax[3,0].set_ylabel("")
ax[3,0].set_xlabel("")
#ax[3,0].yaxis.set_ticklabels([])

sns.ecdfplot(data=df9, x=g, ax=ax[4,0], stat = "count")
sns.ecdfplot(data=df10, x=h, ax=ax[4,0], stat = "count")
ax[4,0].set_xlim([0, 60])
ax[4,0].set_ylabel("")
ax[4,0].set_xlabel("")
#ax[4,0].yaxis.set_ticklabels([])


sns.ecdfplot(data=df11, x=i, ax=ax[5,0], stat = "count")
sns.ecdfplot(data=df12, x=j, ax=ax[5,0], stat = "count")
ax[5,0].set_xlim([0, 60])



#Column 2

sns.ecdfplot(data=df13, x=k, ax=ax[0,1], stat = "count")
sns.ecdfplot(data=df14, x=l, ax=ax[0,1], stat = "count")
ax[0,1].set_xlim([0, 60])
ax[0,1].set_ylabel("")
ax[0,1].set_xlabel("")
#ax[0,1].yaxis.set_ticklabels([])

sns.ecdfplot(data=df15, x=m, ax=ax[1,1], stat = "count")
sns.ecdfplot(data=df16, x=n, ax=ax[1,1], stat = "count")
ax[1,1].set_xlim([0, 200])
ax[1,1].set_ylabel("")
ax[1,1].set_xlabel("")
#ax[1,1].yaxis.set_ticklabels([])

sns.ecdfplot(data=df17, x=o, ax=ax[2,1], stat = "count")
sns.ecdfplot(data=df18, x=p, ax=ax[2,1], stat = "count")
ax[2,1].set_xlim([0, 75])
ax[2,1].set_ylabel("")
ax[2,1].set_xlabel("")
#ax[2,1].yaxis.set_ticklabels([])

sns.ecdfplot(data=df19, x=q, ax=ax[3,1], stat = "count")
sns.ecdfplot(data=df20, x=r, ax=ax[3,1], stat = "count")
ax[3,1].set_xlim([0, 80])
ax[3,1].set_ylabel("")
ax[3,1].set_xlabel("")
#ax[3,1].yaxis.set_ticklabels([])

sns.ecdfplot(data=df21, x=s, ax=ax[4,1], stat = "count")
sns.ecdfplot(data=df22, x=t, ax=ax[4,1], stat = "count")
ax[4,1].set_xlim([0, 50])
ax[4,1].set_ylabel("")
#ax[4,1].yaxis.set_ticklabels([])



fig.tight_layout(pad=0.5)
plt.savefig("CountEcdf.svg", format="svg")





