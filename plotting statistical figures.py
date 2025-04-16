import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from string import ascii_letters
import palettable
import seaborn as sns


############### Figure 6a ###############
# The file "Source Data.xlsx" is stored in the directory "Technical validation"
df_scene = pd.read_excel('Technical validation\Source Data.xlsx',sheet_name='Figure 6a')

colors = ['#DB7272',
         '#C6A550',
         '#A1D4A2',
         '#3C518F',
         '#38917E',
         '#B384BA',
         '#989ED9',
         '#4D0085']

# Pie
dpi = 300
plt.figure(figsize=(12,6))
plt.pie(x=list(df_scene['Proportion(%)']),
        # labels=list(df_scene['Scene']),
        labels=None,
        colors=colors,
        autopct='%.2f%%',
        radius=1.3,
        pctdistance = 0.75,
        explode = (0.02,0.02,0.01,0.02,0.02,0.02,0.01,0.02),
        startangle=90,
        counterclock=False,
        labeldistance = 1.2,
        textprops={'fontsize': 14,
                    'color': 'white',
                    'fontfamily':'Arial'})
plt.legend(title='Scene',
           labels = list(df_scene['Scene']),
           fontsize=14,
           loc='best',
           title_fontsize = 14,
           bbox_to_anchor=(1, 0, 0.5, 1))
# plt.savefig('fig4a.png',dpi=dpi,bbox_inches='tight')
plt.savefig('Figure_6a.svg',format='svg')


############### Figure 6b ###############
# Read the data from an Excel file
df_vessel = pd.read_excel('Technical validation\Source Data.xlsx',sheet_name='Figure 6b')

# Ensure that the colors of the bar charts match the colors of the vessels in the flowchart
# Arteries: red (220, 20, 60), Veins: blue (140, 67, 86), Other vessels: green (0, 255, 127)
# When calling plt.barh, the RGBA color values should be between 0 and 1 (float), not 0 to 255 (integer). 
# A represents opacity, ranging from 0 (fully transparent) to 1 (fully opaque). The default is 1.
# Therefore, RGB values should be divided by 255 to get a float between 0 and 1, and the alpha value is set to 1 (fully opaque).

# Bar Chart S1
dpi = 300
plt.figure(figsize=(4800/dpi, 900/dpi), dpi=dpi)
data = [668, 0, 0, 0]
plt.barh([0, 0.5, 1, 1.5], data, height=0.4, color=(11/255, 172/255, 94/255), edgecolor='black')  # Change color to match flowchart

# Customize x-ticks
my_x_ticks = np.arange(0, 1010, 200)
plt.xticks(my_x_ticks)
plt.yticks([])  # Hide y-ticks
plt.xticks(fontproperties='Arial', size=18)
ax = plt.gca()
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig("Figure_6b-S1.svg", format='svg')

# Bar Chart S2
dpi = 300
plt.figure(figsize=(4800/dpi, 900/dpi), dpi=dpi)
data = [423, 0, 0, 0]
plt.barh([0, 0.5, 1, 1.5], data, height=0.4, color=(11/255, 172/255, 94/255), edgecolor='black')  # Change color to match flowchart

# Customize x-ticks
plt.xticks(my_x_ticks)
plt.yticks([])  # Hide y-ticks
plt.xticks(fontproperties='Arial', size=18)
ax = plt.gca()
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.legend()
plt.savefig("Figure_6b-S2.svg", format='svg')

# Bar Chart S3
dpi = 300
plt.figure(figsize=(4800/dpi, 900/dpi), dpi=dpi)
data = [0, 582, 845, 0]
plt.barh([0, 0.5, 1, 1.5], data, height=0.4, color=[(220/255, 20/255, 60/255), (220/255, 20/255, 60/255), 
                                                   (0/255, 191/255, 255/255), (220/255, 20/255, 60/255)], edgecolor='black')  # Adjust color to match flowchart

# Customize x-ticks
plt.xticks(my_x_ticks)
plt.yticks([])  # Hide y-ticks
plt.xticks(fontproperties='Arial', size=18)
ax = plt.gca()
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig("Figure_6b-S3.svg", format='svg')

# Bar Chart S4
dpi = 300
plt.figure(figsize=(4800/dpi, 900/dpi), dpi=dpi)
data = [0, 348, 0, 0]
plt.barh([0, 0.5, 1, 1.5], data, height=0.4, color=[(220/255, 20/255, 60/255), (220/255, 20/255, 60/255), 
                                                   (0/255, 191/255, 255/255), (220/255, 20/255, 60/255)], edgecolor='black')  # Adjust color to match flowchart

# Customize x-ticks
plt.xticks(my_x_ticks)
plt.yticks([])  # Hide y-ticks
plt.xticks(fontproperties='Arial', size=18)
ax = plt.gca()
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig("Figure_6b-S4.svg", format='svg')

# Bar Chart S5
dpi = 300
plt.figure(figsize=(4800/dpi, 900/dpi), dpi=dpi)
data = [452, 266, 390, 0]
plt.barh([0, 0.5, 1, 1.5], data, height=0.4, color=[(220/255, 20/255, 60/255), (0, 191/255, 255/255), 
                                                   (220/255, 20/255, 60/255), (0, 255/255, 127/255)], edgecolor='black')  # Adjust color to match flowchart

# Customize x-ticks
plt.xticks(my_x_ticks)
plt.yticks([])  # Hide y-ticks
plt.xticks(fontproperties='Arial', size=18)
ax = plt.gca()
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig("Figure_6b-S5.svg", format='svg')

# Bar Chart S6
dpi = 300
plt.figure(figsize=(4800/dpi, 900/dpi), dpi=dpi)
data = [533, 633, 905, 672]
plt.barh([0, 0.5, 1, 1.5], data, height=0.4, color=[(220/255, 20/255, 60/255), (0/255, 191/255, 255/255), 
                                                   (220/255, 20/255, 60/255), (220/255, 20/255, 60/255)], edgecolor='black')  # Adjust color to match flowchart

# Customize x-ticks
plt.xticks(my_x_ticks)
plt.yticks([])  # Hide y-ticks
plt.xticks(fontproperties='Arial', size=18)
ax = plt.gca()
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig("Figure_6b-S6.svg", format='svg')

# Bar Chart S7
dpi = 300
plt.figure(figsize=(4800/dpi, 900/dpi), dpi=dpi)
data = [87, 308, 0, 0]
plt.barh([0, 0.5, 1, 1.5], data, height=0.4, color=[(0/255, 191/255, 255/255), (0/255, 191/255, 255/255), 
                                                   (0/255, 191/255, 255/255), (220/255, 20/255, 60/255)], edgecolor='black')  # Adjust color to match flowchart

# Customize x-ticks
plt.xticks(my_x_ticks)
plt.yticks([])  # Hide y-ticks
plt.xticks(fontproperties='Arial', size=18)
ax = plt.gca()
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig("Figure_6b-S7.svg", format='svg')

# Bar Chart S8
dpi = 300
plt.figure(figsize=(4800/dpi, 900/dpi), dpi=dpi)
data = [383, 0, 0, 0]
plt.barh([0, 0.5, 1, 1.5], data, height=0.4, color=(11/255, 172/255, 94/255), edgecolor='black')  # Adjust color to match flowchart

# Customize x-ticks
plt.xticks(my_x_ticks)
plt.yticks([])  # Hide y-ticks
plt.xticks(fontproperties='Arial', size=18)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig("Figure_6b-S8.svg", format='svg')

################# Figure 6c ###############
plt.rcParams['font.sans-serif'] = 'Arial'  
plt.figure(figsize=(18, 7)) 
data = pd.read_excel('Technical validation\Source Data.xlsx',sheet_name='Figure 6c')


x  = data['Video ID']
y1 = data['S1']
y2 = data['S2']
y3 = data['S3']
y4 = data['S4']
y5 = data['S5']
y6 = data['S6']
y7 = data['S7']
y8 = data['S8']

linewidth = 0.01
edgecolor = 'black'
width = 0.5
plt.bar(x,y1,                                         width=width,label='S1',color='#DB7272',edgecolor=edgecolor,linewidth=linewidth)
plt.bar(x,y2,bottom=y1,                               width=width,label='S2',color='#C6A550',edgecolor=edgecolor,linewidth=linewidth)
plt.bar(x,y3,bottom=y1+y2,                            width=width,label='S3',color='#A1D4A2',edgecolor=edgecolor,linewidth=linewidth)
plt.bar(x,y4,bottom=y1+y2+y3,                         width=width,label='S4',color='#3C518F',edgecolor=edgecolor,linewidth=linewidth)
plt.bar(x,y5,bottom=y1+y2+y3+y4,                      width=width,label='S5',color='#38917E',edgecolor=edgecolor,linewidth=linewidth)
plt.bar(x,y6,bottom=y1+y2+y3+y4+y5,                   width=width,label='S6',color='#B384BA',edgecolor=edgecolor,linewidth=linewidth)
plt.bar(x,y7,bottom=y1+y2+y3+y4+y5+y6,                width=width,label='S7',color='#989ED9',edgecolor=edgecolor,linewidth=linewidth)
plt.bar(x,y8,bottom=y1+y2+y3+y4+y5+y6+y7,             width=width,label='S8',color='#4D0085',edgecolor=edgecolor,linewidth=linewidth)

# x_ticks = list(data['ID'])
plt.xticks(x)
plt.xlim(-0.5, max(x) + 0.5)

plt.yticks(range(0,300,50)) 

plt.tick_params(axis='x',length=4)
plt.xlabel('Video ID',fontsize=14)
plt.ylabel('Frame Count',fontsize=14)

ax = plt.gca()
# ax.spines['bottom'].set_visible(False)
# ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


# plt.tight_layout()
# plt.savefig('stack_bar.png', dpi=500)
plt.savefig('Figure_6c.svg', format='svg')

############### Figure 6d ############### 
# Data
categories = ['LapGC-KVAD-30', 'Training Set', 'Validation Set', 'Test Set']
s1 = [0.125966434, 0.12217833, 0.134090909, 0.133105802]
s2 = [0.07976617, 0.076467269, 0.080681818, 0.092150171]
s3 = [0.234961343, 0.231659142, 0.251136364, 0.232081911]
s4 = [0.065623232, 0.072799097, 0.048863636, 0.053469852]
s5 = [0.117857816, 0.123306998, 0.104545455, 0.109215017]
s6 = [0.236092778, 0.235045147, 0.25, 0.226393629]
s7 = [0.067508957, 0.068566591, 0.0625, 0.068259386]
s8 = [0.07222327, 0.069977427, 0.068181818, 0.085324232]

data = np.array([s1, s2, s3, s4, s5, s6, s7, s8])

# Set global font
plt.rcParams['font.sans-serif'] = 'Arial'

# Color settings
colors = [
    '#DB7272',  # S1
    '#C6A550',  # S2
    '#A1D4A2',  # S3
    '#3C518F',  # S4
    '#38917E',  # S5
    '#B384BA',  # S6
    '#989ED9',  # S7
    '#4D0085'   # S8
]

# Create horizontal stacked bar chart
fig, ax = plt.subplots(figsize=(18, 4))
left = np.zeros(len(categories))

# Invert Y-axis to display from top to bottom
ax.invert_yaxis()

# Plot stacked bars
for i, color in enumerate(colors):
    ax.barh(categories, data[i], left=left, color=color, height=0.6, edgecolor='black', linewidth=0.5)
    left += data[i]

# Adjust tick label size
ax.tick_params(axis='y', labelsize=14)

# Add labels and border settings
ax.set_xlabel('Proportion(%)', fontsize=14)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('figure_6d.svg', dpi=300)