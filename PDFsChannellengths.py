#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:15:25 2021

@author: gryphengoss
"""

#os.getcwd()



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
import plotly

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
#xa = (x/x.count()*100)
#print(xa)

y = df2['Length']
#ya = (y/y.count()*100)
#print(ya)


#Hallo
a = df3['Length']
#aa = (a/a.count()*100)
b = df4['Length']
a = df3['Length']
#ba = (b/b.count()*100)
#print(ba)
#print(aa)
a.count()
b.count()



#Slims
c = df5['Length']
d = df6['Length']
c.count()
d.count()

#Meade
e = df7['Length']
f = df8['Length']
e.count()
f.count()

#NWRobs
g = df9['Length']
h = df10['Length']
g.count()
h.count()


#Susitna
i = df11['Length']
j = df12['Length']
i.count()
j.count()

#Kask
k = df13['Length']
l = df14['Length']
k.count()
l.count()

#Tulsequah
m = df15['Length']
n = df16['Length']
m.count()
n.count()

#Lillooet
o = df17['Length']
p = df18['Length']
o.count()
p.count()

#ActRobs
q = df19['Length']
r = df20['Length']
r.count()
q.count()

#KukakBay
s = df21['Length']
t = df22['Length']
s.count()
t.count()





sns.set(font_scale=2)
sns.set_style("white")
#sns.set(rc={'axes.facecolor':'white', 'figure.facecolor':'white'})

fig, ax = plt.subplots(6,2,sharex=False, figsize=(17,16))
#fig.suptitle('Variation in Channel Widths (m)')

 

# seaborn histogram - Klinaklini before -> after
sns.distplot(x, ax=ax[0,0], bins=range(0, 300, 25), hist = True, kde=False, 
             color = 'grey',
             hist_kws={'edgecolor':'grey'})
sns.distplot(y, ax=ax[0,0],bins=range(0, 300, 25), hist=True, kde=False, 
             color = 'black',
             hist_kws={'edgecolor':'black'})
ax[0,0].set_ylim([0, 100])
ax[0,0].set_xlim([0, 300])
#ax[0,0].set_title('Klinaklini Glacier')


# seaborn histogram - Hallo before-> after
sns.distplot(a, ax=ax[1,0],bins=range(0, 60, 5),hist=True, kde=False, 
             color = 'grey',
             hist_kws={'edgecolor':'grey'})
sns.distplot(b, ax=ax[1,0],bins=range(0, 60, 5),hist=True, kde=False, 
             color = 'black',
             hist_kws={'edgecolor':'black'})
ax[1,0].set_ylim([0, 100])
ax[1,0].set_xlim([0, 60])
#ax[1,0].set_title('Hallo Glacier')

# seaborn histogram - Slims before-> after
sns.distplot(c, ax=ax[2,0],bins=range(0, 300, 25), hist=True, kde=False, 
             color = 'grey',
             hist_kws={'edgecolor':'grey'})
sns.distplot(d, ax=ax[2,0],bins=range(0, 300, 25),hist=True, kde=False, 
             color = 'black',
             hist_kws={'edgecolor':'black'})
ax[2,0].set_ylim([0, 100])
ax[2,0].set_xlim([0, 300])
#ax[2,0].set_title('Kaskawulsh Glacier - Slims')

# seaborn histogram - Meade before-> after
sns.distplot(e, ax=ax[3,0],bins=range(0, 200, 10),hist=True, kde=False, 
             color = 'grey',
             hist_kws={'edgecolor':'grey'})
sns.distplot(f, ax=ax[3,0],bins=range(0, 200, 10),hist=True, kde=False, 
             color = 'black',
             hist_kws={'edgecolor':'black'})
ax[3,0].set_ylim([0, 100])
ax[3,0].set_xlim([0, 200])
#ax[3,0].set_title('Meade Glacier')


# seaborn histogram - NWRobs before-> after
sns.distplot(g, ax=ax[4,0],bins=range(0, 100, 10), hist=True, kde=False, 
             color = 'grey',
             hist_kws={'edgecolor':'grey'})
sns.distplot(h, ax=ax[4,0],bins=range(0, 100, 10),hist=True, kde=False, 
             color = 'black',
             hist_kws={'edgecolor':'black'})
ax[4,0].set_ylim([0, 100])
ax[4,0].set_xlim([0, 100])
#ax[4,0].set_title('NW Robs Glacier')

# seaborn histogram - Susitna before-> after
sns.distplot(i, ax=ax[5,0],bins=range(0, 80, 10),hist=True, kde=False, 
             color = 'grey',
             hist_kws={'edgecolor':'grey'})
sns.distplot(j, ax=ax[5,0],bins=range(0, 80, 10),hist=True, kde=False, 
             color = 'black',
             hist_kws={'edgecolor':'black'})
ax[5,0].set_ylim([0, 100])
ax[5,0].set_xlim([0, 80])
#ax[5,0].set_title('Susitna Glacier')

# seaborn histogram - Kaskwaulsh River before-> after
sns.distplot(k, ax=ax[0,1],bins=range(0, 60, 5), hist=True, kde=False, 
             color = 'grey',
             hist_kws={'edgecolor':'grey'})
sns.distplot(l, ax=ax[0,1],bins=range(0, 60, 5),hist=True, kde=False, 
             color = 'black',
             hist_kws={'edgecolor':'black'})
ax[0,1].set_ylim([0, 100])
ax[0,1].set_xlim([0, 60])
#ax[0,1].set_title('Kaskawulsh River')

# seaborn histogram - Tulsequah Glacier before-> after
sns.distplot(m, ax=ax[1,1],bins=range(0, 200, 10),hist=True, kde=False, 
             color = 'grey',
             hist_kws={'edgecolor':'grey'})
sns.distplot(n, ax=ax[1,1],bins=range(0, 200, 10), hist=True, kde=False, 
             color = 'black',
             hist_kws={'edgecolor':'black'})
ax[1,1].set_ylim([0, 100])
ax[1,1].set_xlim([0, 200])
#ax[1,1].set_title('Tulsequah Glacier')


# seaborn histogram - Lillooet Glacier before-> after
sns.distplot(o, ax=ax[2,1],bins=range(0, 80, 10),hist=True, kde=False, 
             color = 'grey',
             hist_kws={'edgecolor':'grey'})
sns.distplot(p, ax=ax[2,1],bins=range(0, 80, 10),hist=True, kde=False, 
             color = 'black',
             hist_kws={'edgecolor':'black'})
ax[2,1].set_ylim([0, 100])
ax[2,1].set_xlim([0, 80])
#ax[2,1].set_title('Lillooet Glacier')

# seaborn histogram - Actual Robs Glacier before-> after
sns.distplot(q, ax=ax[3,1],bins=range(0, 80, 10),hist=True, kde=False, 
             color = 'grey',
             hist_kws={'edgecolor':'grey'})
sns.distplot(r, ax=ax[3,1],bins=range(0, 80, 10), hist=True, kde=False, 
             color = 'black',
             hist_kws={'edgecolor':'black'})
ax[3,1].set_ylim([0, 100])
ax[3,1].set_xlim([0, 80])
#ax[3,1].set_title('Robertson Glacier')

# seaborn histogram - Kukak Bay Glacier before-> after
sns.distplot(s, ax=ax[4,1],bins=range(0, 40, 5),hist=True, kde=False, 
             color = 'grey',
             hist_kws={'edgecolor':'grey'})
sns.distplot(t, ax=ax[4,1],bins=range(0, 40, 5),hist=True, kde=False, 
             color = 'black',
             hist_kws={'edgecolor':'black'})
ax[4,1].set_ylim([0, 100])
ax[4,1].set_xlim([0, 40])
#ax[4,1].set_title('Kukak Bay Glacier')



fig.tight_layout(pad=0.08)


# Add labels
plt.title('')
plt.xlabel('')
plt.ylabel('')
