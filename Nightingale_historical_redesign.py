import os
import gc
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show, rc
import pandas as pd
import numpy as np
os.chdir("D:\\School\\Spring 2023\\Data Vis\\Historical Redesign")
Nightingale = pd.read_csv("nightingale.csv")

Nightingale.loc[0,"Label"] = "APRIL\n1854"
Nightingale.loc[9,"Label"] = "JANUARY\n1855"
Nightingale.loc[11,"Label"] = "MARCH\n1855"
Nightingale.loc[12,'Label'] = "APRIL\n1855"
Nightingale.loc[21,'Label'] = "JANUARY\n1856"

#%%
plt.figure(figsize=(10,10), facecolor="#ece2df")
ax = plt.subplot(111, polar=True, facecolor="#ece2df")
ax.set_theta_direction(-1)
ax.set_theta_zero_location("W", offset=-15)
plt.axis('off')



angles = np.arange(0, 2*np.pi, np.pi/6)
ArmyHeights = (Nightingale.loc[0:11,'Army'] - np.pi/12)**(1/2)
DiseaseHeights = (Nightingale.loc[0:11,'Disease'] - np.pi/12)**(1/2)
WoundsHeights = (Nightingale.loc[0:11,'Wounds'] - np.pi/12)**(1/2)
WoundsHeights.iloc[0:4] = 0
OtherHeights = (Nightingale.loc[0:11,'Other'] - np.pi/12)**(1/2)


bars = ax.bar(
    x=angles,
    height=DiseaseHeights,
    width=np.pi/6,
    bottom=0,
    linewidth=0.1,
    edgecolor="black",
    color="#adbfc3"
)

bars3 = ax.bar(
    x=angles,
    height=OtherHeights,
    width=np.pi/6,
    bottom=0,
    linewidth=1,
    edgecolor="black",
    color="#c96363",
    alpha=0.5
)

bars2 = ax.bar(
    x=angles,
    height=WoundsHeights,
    width=np.pi/6,
    bottom=0,
    linewidth=1,
    edgecolor="black",
    color="#8a8178",
    alpha = 0.5
)

for bar, angle, height, label in zip(bars, angles, DiseaseHeights, Nightingale.loc[0:11, "Label"]):
    rotation = np.rad2deg((2*np.pi)-angle)
    labelheight=3
    alignment = ""
    if angle > 5*np.pi/12 and angle < 17*np.pi/12:
        rotation = rotation + 74
    else:
        rotation = rotation +74
    if height < 10:
        labelheight = 9
    else:
        labelheight = bar.get_height() + 2
    ax.text(
        x=angle,
        y=labelheight,
        s=label,
        ha="center",
        va='center',
        rotation=rotation,
        rotation_mode="anchor",
        size=8,
        font="Arial",
        color="#302b27")

plt.savefig('Roseplot_output1.png',
            dpi=750)

#%%
plt.figure(figsize=(10,10), facecolor="#ece2df")
ax = plt.subplot(111, polar=True, facecolor="#ece2df")
ax.set_theta_direction(-1)
ax.set_theta_zero_location("W", offset=-15)
plt.axis('off')

ArmyHeights2 = (Nightingale.loc[12:23,'Army'] - np.pi/12)**(1/2)
DiseaseHeights2 = (Nightingale.loc[12:23,'Disease'] - np.pi/12)**(1/2)
WoundsHeights2 = (Nightingale.loc[12:23,'Wounds'] - np.pi/12)**(1/2)
WoundsHeights2.loc[22:23] = 0
OtherHeights2 = (Nightingale.loc[12:23,'Other'] - np.pi/12)**(1/2)

bars = ax.bar(
    x=angles,
    height=DiseaseHeights2,
    width=np.pi/6,
    bottom=0,
    linewidth=0.1,
    edgecolor="black",
    color="#adbfc3"
)

bars3 = ax.bar(
    x=angles,
    height=OtherHeights2,
    width=np.pi/6,
    bottom=0,
    linewidth=1,
    edgecolor="black",
    color="#c96363",
    alpha=0.5
)

bars2 = ax.bar(
    x=angles,
    height=WoundsHeights2,
    width=np.pi/6,
    bottom=0,
    linewidth=1,
    edgecolor="black",
    color="#8a8178",
    alpha=0.5
)

for bar, angle, height, label in zip(bars, angles, DiseaseHeights2, Nightingale.loc[0:11,"Label"]):
    rotation = np.rad2deg((2*np.pi)-angle)
    alignment = ""
    if angle > 5*np.pi/12 and angle < 17*np.pi/12:
        rotation = rotation + 74
    else:
        rotation = rotation +74
    if height < 18:
        labelheight = 17.5
    else:
        labelheight = bar.get_height() + 1.3
    ax.text(
        x=angle,
        y=labelheight,
        s=label,
        ha="center",
        va='center',
        rotation=rotation,
        rotation_mode="anchor",
        size=12,
        font="Arial",
        color="#302b27")

plt.savefig('Roseplot_output2.png',
            dpi=750)
#%%
