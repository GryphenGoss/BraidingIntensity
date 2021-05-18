#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:02:38 2021

@author: gryphengoss
"""



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
import plotly
import matplotlib.ticker as ticker
from matplotlib.pyplot import figure
from matplotlib.ticker import StrMethodFormatter
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

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
#a = df3['Length']
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


fig = figure(num=None, figsize=(9, 16))
style = dict(size=12, color='black')

#Klinaklini
plt.subplot(6, 2, 1)
plt.hist(x, weights=np.ones(len(x)) / len(x), bins = np.linspace(0, 300, 25), alpha = 0.3, color = "grey")
plt.hist(y, weights=np.ones(len(y)) / len(y), bins = np.linspace(0, 300, 25), alpha = 0.3, color = "black")
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(174,0.30,"Klinaklini", ha='left', **style)
plt.text(174,0.20,"n$_{T1}=183 n_{T2}$=130", ha='left', **style)
plt.gca().legend(('Time 1','Time 2'), loc = "upper center", bbox_to_anchor=(0.4, 1))

#Hallo
plt.subplot(6, 2, 2)
plt.hist(a, weights=np.ones(len(a)) / len(a), bins = np.linspace(0, 80, 25), alpha = 0.3, color = "grey")
plt.hist(b, weights=np.ones(len(b)) / len(b), bins = np.linspace(0, 80, 25), alpha = 0.3, color = "black")
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(48,0.30,"Hallo", ha='left', **style)
plt.text(48,0.20,"n$_{T1}=122 n_{T2}$=36", ha='left', **style)

#Slims
plt.subplot(6, 2, 3)
plt.hist(c, weights=np.ones(len(c)) / len(c), bins = np.linspace(0, 100, 25), alpha = 0.3, color = "grey")
plt.hist(d, weights=np.ones(len(d)) / len(d), bins = np.linspace(0, 100, 25), alpha = 0.3, color = "black")
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(57,0.30,"KG - Ä’äy Chù", ha='left', **style)
plt.text(57,0.20,"n$_{T1}=266 n_{T2}$=177", ha='left', **style)

#Meade
plt.subplot(6, 2, 4)
plt.hist(e, weights=np.ones(len(e)) / len(e), bins = np.linspace(0, 100, 25), alpha = 0.3, color = "grey")
plt.hist(f, weights=np.ones(len(f)) / len(f), bins = np.linspace(0, 100, 25), alpha = 0.3, color = "black")
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(57,0.30,"Meade", ha='left', **style)
plt.text(57,0.20,"n$_{T1}=251 n_{T2}$=130", ha='left', **style)

#NWRobertson
plt.subplot(6, 2, 5)
plt.hist(g, weights=np.ones(len(g)) / len(g), bins = np.linspace(0, 100, 25), alpha = 0.3, color = "grey")
plt.hist(h, weights=np.ones(len(h)) / len(h), bins = np.linspace(0, 100, 25), alpha = 0.3, color = "black")
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(60,0.30,"NW of Robertson", ha='left', **style)
plt.text(60,0.20,"n$_{T1}=204 n_{T2}$=79", ha='left', **style)

#Susitna
plt.subplot(6, 2, 6)
plt.hist(i, weights=np.ones(len(i)) / len(i), bins = np.linspace(0, 80, 25), alpha = 0.3, color = "grey")
plt.hist(j, weights=np.ones(len(j)) / len(j), bins = np.linspace(0, 80, 25), alpha = 0.3, color = "black")
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(43,0.30,"East Fork of Susitna", ha='left', **style)
plt.text(43,0.20,"n$_{T1}=238 n_{T2}$=108", ha='left', **style)

#Kaskawulsh
plt.subplot(6, 2, 7)
plt.hist(k, weights=np.ones(len(k)) / len(k), bins = np.linspace(0, 100, 25), alpha = 0.3, color = "grey")
plt.hist(l, weights=np.ones(len(l)) / len(l), bins = np.linspace(0, 100, 25), alpha = 0.3, color = "black")
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(61,0.30,"KG - Kaskawulsh", ha='left', **style)
plt.text(61,0.20,"n$_{T1}=113 n_{T2}$=61", ha='left', **style)

#Tulsequah
plt.subplot(6, 2, 8)
plt.hist(m, weights=np.ones(len(m)) / len(m), bins = np.linspace(0, 100, 25), alpha = 0.3, color = "grey")
plt.hist(n, weights=np.ones(len(n)) / len(n), bins = np.linspace(0, 100, 25), alpha = 0.3, color = "black")
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(61,0.30,"Tulsequah", ha='left', **style)
plt.text(61,0.20,"n$_{T1}=135 n_{T2}$=66", ha='left', **style)

#Lilooet
plt.subplot(6, 2, 9)
plt.hist(o, weights=np.ones(len(o)) / len(o), bins = np.linspace(0, 100, 25), alpha = 0.3, color = "grey")
plt.hist(p, weights=np.ones(len(p)) / len(p), bins = np.linspace(0, 100, 25), alpha = 0.3, color = "black")
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(61,0.30,"Lillooet", ha='left', **style)
plt.text(61,0.20,"n$_{T1}=163 n_{T2}$=93", ha='left', **style)

#Actual_Robertson
plt.subplot(6, 2, 10)
plt.hist(q, weights=np.ones(len(q)) / len(q), bins = np.linspace(0, 50, 25), alpha = 0.3, color = "grey")
plt.hist(r, weights=np.ones(len(r)) / len(r), bins = np.linspace(0, 50, 25), alpha = 0.3, color = "black")
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(27,0.30,"Robertson (control)", ha='left', **style)
plt.text(27,0.20,"n$_{T1}=55 n_{T2}$=57", ha='left', **style)
plt.xlabel('Length (m)', fontsize=12)

#Kukak Bay
plt.subplot(6, 2, 11)
plt.hist(s, weights=np.ones(len(s)) / len(s), bins = np.linspace(0, 40, 25), alpha = 0.3, color = "grey")
plt.hist(t, weights=np.ones(len(t)) / len(t), bins = np.linspace(0, 40, 25), alpha = 0.3, color = "black")
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(21,0.30,"Kukak Bay (control)", ha='left', **style)
plt.text(21,0.20,"n$_{T1}=266 n_{T2}$=177", ha='left', **style)
plt.xlabel('Length (m)', fontsize=12)

fig.tight_layout(pad=0.8)
fig.text(0.008, 0.5, 'Percent of Channels', ha='center', va='center', rotation='vertical')
plt.show()











    
    
    


