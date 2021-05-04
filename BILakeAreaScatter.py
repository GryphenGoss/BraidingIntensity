#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 16:14:19 2021

@author: gryphengoss
"""



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
import plotly

file="/Users/gryphengoss/Desktop/Python_Plotting/TplotsC.xls"

#Load spreadsheet
x1 = pd.ExcelFile(file)

#Print the sheet names
#print(x1.sheet_names)
#Load a sheet into a dataframe by name of: df1
df = x1.parse("TplotsC")

import plotly.express as px
import plotly.io as pio
pio.templates
pio.templates.default = "simple_white"
fig = px.scatter(df, x="Lake Area (Km^2)", y="Braiding Intensity", color="Site",
                 size='MeanWidth')


plotly.offline.plot(fig)


