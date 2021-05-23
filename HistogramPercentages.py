#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:02:38 2021

@author: gryphengoss
"""

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
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
y = df2['Length']
xm=(x.median())
ym=(y.median())
print(xm)
print(ym)

#Hallo
a = df3['Length']
b = df4['Length']
am = a.median()
bm = b.median()
print(am)
print(bm)


#Slims
c = df5['Length']
d = df6['Length']
c.count()
d.count()
cm = c.median()
dm = d.median()
print(cm)
print(dm)


#Meade
e = df7['Length']
f = df8['Length']
e.count()
f.count()
em = e.median()
fm = f.median()
print(em)
print(fm)


#NWRobs
g = df9['Length']
h = df10['Length']
g.count()
h.count()
gm = g.median()
hm = h.median()
print(gm)
print(hm)


#Susitna
i = df11['Length']
j = df12['Length']
i.count()
j.count()
im = i.median()
jm = j.median()
print(im)
print(jm)

#Kask
k = df13['Length']
l = df14['Length']
k.count()
l.count()
km = k.median()
lm = l.median()
print(km)
print(lm)

#Tulsequah
m = df15['Length']
n = df16['Length']
m.count()
n.count()
mm = m.median()
nm = n.median()
print(mm)
print(nm)

#Lillooet
o = df17['Length']
p = df18['Length']
o.count()
p.count()
om = o.median()
pm = p.median()
print(om)
print(pm)

#ActRobs
q = df19['Length']
r = df20['Length']
r.count()
q.count()
qm = q.median()
rm = r.median()
print(qm)
print(rm)

#KukakBay
s = df21['Length']
t = df22['Length']
s.count()
t.count()
sm = s.median()
tm = t.median()
print(sm)
print(tm)


fig = figure(num=None, figsize=(9, 16))
style = dict(size=13, color='black')

#Klinaklini
plt.subplot(6, 2, 1)
plt.hist(x, weights=np.ones(len(x)) / len(x), bins = np.linspace(0, 300, 25), facecolor = "none", edgecolor='black', linewidth=2)
plt.hist(y, weights=np.ones(len(y)) / len(y), bins = np.linspace(0, 300, 25), facecolor = "none", edgecolor='red', linewidth=2)
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(145,0.17,"Klinaklini", ha='left', **style)
plt.text(145,0.10,'n$_{T1}=183, n_{T2}$=130', ha='left', **style)
plt.annotate('m =  35.0',xy=(xm, 0.30),
            xytext=(58.7, 0.31))
plt.annotate('m =  35.0',xy=(ym, 0.30),  
            xytext=(65, 0.27))
plt.gca().legend(('Time 1','Time 2'), loc = "upper center", bbox_to_anchor=(0.6, 1))
plt.vlines(xm, 0, 0.30, color="black")
plt.vlines(ym, 0, 0.26, color="red")

#Hallo
plt.subplot(6, 2, 2)
plt.hist(a, weights=np.ones(len(a)) / len(a), bins = np.linspace(0, 65, 25), facecolor = "none", edgecolor='black', linewidth=2)
plt.hist(b, weights=np.ones(len(b)) / len(b), bins = np.linspace(0, 65, 25), facecolor = "none", edgecolor='red', linewidth=2)
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(36,0.15,"Hallo", ha='left', **style)
plt.text(36,0.10,"n$_{T1}=122, n_{T2}$=36", ha='left', **style)
plt.annotate('m =  13.8', xy=(am, 0.30),
            xytext=(am, 0.31))
plt.annotate('m =  22.5', xy=(bm, 0.30), 
            xytext=(bm, 0.27))
plt.vlines(am, 0, 0.30, color="black")
plt.vlines(bm, 0, 0.26, color="red")

#Slims
plt.subplot(6, 2, 3)
plt.hist(c, weights=np.ones(len(c)) / len(c), bins = np.linspace(0, 100, 25), facecolor = "none", edgecolor='black', linewidth=2)
plt.hist(d, weights=np.ones(len(d)) / len(d), bins = np.linspace(0, 100, 25), facecolor = "none", edgecolor='red', linewidth=2)
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(53,0.15,"KG - Ä’äy Chù", ha='left', **style)
plt.text(53,0.10,"n$_{T1}=266, n_{T2}$=177", ha='left', **style)
plt.annotate('m =  25.7', xy=(cm, 0.30),
            xytext=(cm, 0.31))
plt.annotate('m =  29.1', xy=(dm, 0.30), 
            xytext=(dm, 0.27))
plt.vlines(cm, 0, 0.30, color="black")
plt.vlines(dm, 0, 0.26, color="red")

#Meade
plt.subplot(6, 2, 4)
plt.hist(e, weights=np.ones(len(e)) / len(e), bins = np.linspace(0, 100, 25), facecolor = "none", edgecolor='black', linewidth=2)
plt.hist(f, weights=np.ones(len(f)) / len(f), bins = np.linspace(0, 100, 25), facecolor = "none", edgecolor='red', linewidth=2)
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(52,0.15,"Meade", ha='left', **style)
plt.text(52,0.10,"n$_{T1}=251, n_{T2}$=130", ha='left', **style)
plt.annotate('m =  17.5', xy=(em, 0.30),
            xytext=(em, 0.31))
plt.annotate('m =  24.4', xy=(fm, 0.30), 
            xytext=(fm, 0.27))
plt.vlines(em, 0, 0.30, color="black")
plt.vlines(fm, 0, 0.26, color="red")


#NWRobertson
plt.subplot(6, 2, 5)
plt.hist(g, weights=np.ones(len(g)) / len(g), bins = np.linspace(0, 100, 25), facecolor = "none", edgecolor='black', linewidth=2)
plt.hist(h, weights=np.ones(len(h)) / len(h), bins = np.linspace(0, 100, 25), facecolor = "none", edgecolor='red', linewidth=2)
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(55,0.15,"NW of Robertson", ha='left', **style)
plt.text(55,0.10,"n$_{T1}=204, n_{T2}$=79", ha='left', **style)
plt.annotate('m =  12.2', xy=(gm, 0.30),
            xytext=(gm, 0.31))
plt.annotate('m =  17.2', xy=(hm, 0.30), 
            xytext=(hm, 0.27))
plt.vlines(gm, 0, 0.30, color="black")
plt.vlines(hm, 0, 0.26, color="red")

#Susitna
plt.subplot(6, 2, 6)
plt.hist(i, weights=np.ones(len(i)) / len(i), bins = np.linspace(0, 70, 25), facecolor = "none", edgecolor='black', linewidth=2)
plt.hist(j, weights=np.ones(len(j)) / len(j), bins = np.linspace(0, 70, 25), facecolor = "none", edgecolor='red', linewidth=2)
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(34,0.15,"East Fork of Susitna", ha='left', **style)
plt.text(34,0.10,"n$_{T1}=238, n_{T2}$=108", ha='left', **style)
plt.annotate('m =  14.2', xy=(im, 0.30),
            xytext=(im, 0.31))
plt.annotate('m =  16.1', xy=(jm, 0.30), 
            xytext=(jm, 0.27))
plt.vlines(im, 0, 0.30, color="black")
plt.vlines(jm, 0, 0.26, color="red")

#Kaskawulsh
plt.subplot(6, 2, 7)
plt.hist(k, weights=np.ones(len(k)) / len(k), bins = np.linspace(0, 65, 25), facecolor = "none", edgecolor='black', linewidth=2)
plt.hist(l, weights=np.ones(len(l)) / len(l), bins = np.linspace(0, 65, 25), facecolor = "none", edgecolor='red', linewidth=2)
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(36,0.15,"KG - Kaskawulsh", ha='left', **style)
plt.text(36,0.10,"n$_{T1}=113, n_{T2}$=61", ha='left', **style)
plt.annotate('m =  12.8', xy=(km, 0.30),
            xytext=(km, 0.31))
plt.annotate('m =  20.1', xy=(lm, 0.30), 
            xytext=(lm-1, 0.27))
plt.vlines(km, 0, 0.30, color="black")
plt.vlines(lm, 0, 0.26, color="red")

#Tulsequah
plt.subplot(6, 2, 8)
plt.hist(m, weights=np.ones(len(m)) / len(m), bins = np.linspace(0, 100, 25), facecolor = "none", edgecolor='black', linewidth=2)
plt.hist(n, weights=np.ones(len(n)) / len(n), bins = np.linspace(0, 100, 25), facecolor = "none", edgecolor='red', linewidth=2)
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(56,0.15,"Tulsequah", ha='left', **style)
plt.text(56,0.10,"n$_{T1}=135, n_{T2}$=66", ha='left', **style)
plt.annotate('m =  30.4', xy=(mm, 0.30),
            xytext=(mm, 0.31))
plt.annotate('m =  49.6', xy=(nm, 0.30), 
            xytext=(nm, 0.27))
plt.vlines(mm, 0, 0.30, color="black")
plt.vlines(nm, 0, 0.26, color="red")

#Lilooet
plt.subplot(6, 2, 9)
plt.hist(o, weights=np.ones(len(o)) / len(o), bins = np.linspace(0, 80, 25), facecolor = "none", edgecolor='black', linewidth=2)
plt.hist(p, weights=np.ones(len(p)) / len(p), bins = np.linspace(0, 80, 25), facecolor = "none", edgecolor='red', linewidth=2)
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(40,0.30,"Lillooet", ha='left', **style)
plt.text(40,0.25,"n$_{T1}=163, n_{T2}$=93", ha='left', **style)
plt.annotate('m =  13.9', xy=(om, 0.30),
            xytext=(om, 0.31))
plt.annotate('m =  19.3', xy=(pm, 0.30), 
            xytext=(pm, 0.27))
plt.vlines(om, 0, 0.30, color="black")
plt.vlines(pm, 0, 0.26, color="red")

#Actual_Robertson
plt.subplot(6, 2, 10)
plt.hist(q, weights=np.ones(len(q)) / len(q), bins = np.linspace(0, 50, 25), facecolor = "none", edgecolor='black', linewidth=2)
plt.hist(r, weights=np.ones(len(r)) / len(r), bins = np.linspace(0, 50, 25), facecolor = "none", edgecolor='red', linewidth=2)
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(25,0.15,"Robertson (control)", ha='left', **style)
plt.text(25,0.10,"n$_{T1}=55, n_{T2}$=57", ha='left', **style)
plt.xlabel('Length (m)', fontsize=12)
plt.annotate('m =  14.4', xy=(qm, 0.30),
            xytext=(qm, 0.31))
plt.annotate('m =  17.6', xy=(rm, 0.30), 
            xytext=(rm, 0.27))
plt.vlines(qm, 0, 0.30, color="black")
plt.vlines(rm, 0, 0.26, color="red")

#Kukak Bay
plt.subplot(6, 2, 11)
plt.hist(s, weights=np.ones(len(s)) / len(s), bins = np.linspace(0, 35, 25), facecolor = "none", edgecolor='black', linewidth=2)
plt.hist(t, weights=np.ones(len(t)) / len(t), bins = np.linspace(0, 35, 25), facecolor = "none", edgecolor='red', linewidth=2)
plt.gca().yaxis.set_major_formatter(FuncFormatter('{0:.0%}'.format))
plt.ylim((0,0.4))
plt.text(17,0.15,"Kukak Bay (control)", ha='left', **style)
plt.text(17,0.10,"n$_{T1}=33, n_{T2}$=34", ha='left', **style)
plt.xlabel('Length (m)', fontsize=12)
plt.annotate('m =  11.1', xy=(sm, 0.30),
            xytext=(sm, 0.31))
plt.annotate('m =  13.4', xy=(tm, 0.30), 
            xytext=(tm, 0.27))
plt.vlines(sm, 0, 0.30, color="black")
plt.vlines(tm, 0, 0.26, color="red")

fig.tight_layout(pad=0.8)
fig.text(0.008, 0.5, 'Percent of Channels', ha='center', va='center', rotation='vertical')
plt.show()












    
    
    


