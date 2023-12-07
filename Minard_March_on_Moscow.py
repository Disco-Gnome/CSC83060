import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn
import numpy as np
import pandas as pd
import geopandas as gpd
import shapely
import matplotlib.patches as patches


# %%
os.chdir("D:\\School\\Spring 2023\\Data Vis\\March on Moscow")
cities = pd.read_csv("Minard_cities.csv")
troops = pd.read_csv("Minard_troops.csv")
temps = pd.read_csv("Minard_temp.csv")
rivers = gpd.read_file("Large_rivers.shp")
# %%
font = {'family': 'Brush Script MT',
        'weight': 'light',
        'size': 6}
mpl.rc('font', **font)

# %%


fig = plt.figure(facecolor="#ffffff")
fig.set_figwidth(12)
fig.set_figheight(9)
plt.suptitle("Carte figurative des pertes successives en hommes de l'Armee Francaise dans la Campagne de Russie 1812-1813\nPressee par M. Minard, Inspecteur General des Ponts en Chausseer en Retraite. Paris, le 20 Novembre 1869",
             fontsize=16)

plt1 = plt.subplot(2,1,1)
plt.scatter(x=cities['long'], y=cities['lat'], alpha=0)

plt.text(23.75,56.5,"Les nombres l'hommes presents som-representes par les largeurs des zones colorees a raison d'un millimetre pour dix mille hommes; ils som de plus ecrits en traverss\n des zones. Le rouge designe les hommes qui entrem en Russie, le noir ceux qui eu portem. _____ Les reseignements qui om servi a dresser la carte om-ete puisea\nPour mieux faire juger a l'oeil la diminution de l'armee, j'ai suppose que les corps, du Prince Jerome en du Marechal Davousi qui avaiem ete detaches sur Minsk\n an Mobilow es om rejoin vers Orscha es Witebsk, avaieu toujours warche avec l'armee.",
         fontsize=11)

plt.text(28.9,57.65,"_________________________",
         fontsize=11)

plt.axis("off")
plt.text(x=cities.long[2]-0.25,y=cities.lat[2]+0.05,s=cities.city[2])
plt.text(x=cities.long[3]+0.5,y=cities.lat[3]-0.1,s=cities.city[3])
plt.text(x=cities.long[6]-0.05,y=cities.lat[6],s=cities.city[6])
plt.text(x=cities.long[7]+0.2,y=cities.lat[7]+0.05,s=cities.city[7])
plt.text(x=cities.long[13]-0.2,y=cities.lat[13]-0.25,s=cities.city[13])
plt.text(x=cities.long[14],y=cities.lat[14]-0.25,s=cities.city[14])
plt.text(x=cities.long[17]+0.1,y=cities.lat[17],s=cities.city[17])
plt.text(x=cities.long[18]+0.6,y=cities.lat[18]-0.25,s=cities.city[18])
plt.text(x=cities.long[19],y=cities.lat[19]-0.25,s=cities.city[19])

plt.text(x=troops.label_long[44]-0.2,
         y=troops.label_lat[44]-0.25,
         s=troops.survivors[44],
         rotation=90-troops.rotation[44])
plt.text(x=troops.label_long[6]+0.1,
         y=troops.label_lat[6]+0.1,
         s=troops.survivors[6],
         rotation=90-troops.rotation[6])
plt.text(x=troops.label_long[8]+0.1,
         y=troops.label_lat[8]+0.15,
         s=troops.survivors[8],
         rotation=90-troops.rotation[8])
plt.text(x=troops.label_long[17]+0.2,
         y=troops.label_lat[17]-0.1,
         s=troops.survivors[17],
         rotation=90-troops.rotation[17])
plt.text(x=troops.label_long[18],
         y=troops.label_lat[18]+0.2,
         s=troops.survivors[18],
         rotation=90-troops.rotation[18])
plt.text(x=troops.label_long[19],
         y=troops.label_lat[19]-0.4,
         s=troops.survivors[19],
         rotation=90-troops.rotation[19])

for i in (0,1,4,5,8,9,10,11,12,15,16):
    plt.text(x=cities.long[i],
             y=cities.lat[i]-0.05,
             s=cities.city[i])

for i in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50):
    if troops.direction[i] == "A":
        plt.plot(troops.long[i:i + 2], troops.lat[i:i + 2],
                 linewidth=20*troops.survivors[i] / 340000,
                 color="#DEC19A")
    else:
        plt.plot(troops.long[i:i + 2], troops.lat[i:i + 2],
                 linewidth=20*troops.survivors[i] / 340000,
                 color="#000000")


for i in (0,3,4,5,7,9,10,11,12,13,20,21,22,23,29,30,31,32,38,39,42,47):
    if troops.direction[i] == "A":
        plt.text(x=troops.label_long[i],
                 y=troops.label_lat[i]+0.1,
                 s=troops.survivors[i],
                 rotation=90-troops.rotation[i])
    else:
        plt.text(x=troops.label_long[i],
                 y=troops.label_lat[i]-0.3,
                 s=troops.survivors[i],
                 rotation=90-troops.rotation[i])

plt.xlim(23,39)
plt.ylim(52,57)

temp_text = ("Zero le 18 8bre.",
             "Pluie 24 8bre.",
             "-9.° le 9 9bre.",
             "-21.° le 14 9bre.",
             "-11.°",
             "-20.° le 28 9bre.",
             "-24.° le 1 9bre.",
             "-30.° le 6 Xbre.",
             "-26.° le 7 Xbre.")

plt2 = plt.subplot(2,1,2)
plt.plot(temps["long"],
         temps["temp"],
         color="black")
plt2.yaxis.tick_right()
plt.xticks()
plt.xlim(23,39)
plt.yticks([-30,-25,-20,-15,-10,-5,0],["-30 degrês","-25","-20","-15","-10","-5","Zero le 18 8bre."])
plt.xticks([])
plt.grid(axis = 'y')
for i in (3,5):
    plt.text(x=temps.long[i]-0.4,
             y=temps.temp[i]-2,
             s=temp_text[i])
for i in (1,2,6):
    plt.text(x=temps.long[i],
             y=temps.temp[i]-2.5,
             s=temp_text[i])
plt.text(x=temps.long[4]-0.1,
         y=temps.temp[4]-2,
         s=temp_text[4])
plt.text(x=temps.long[8]-1,
         y=temps.temp[8]-1.5,
         s=temp_text[8])
plt.text(x=temps.long[7]-0.5,
         y=temps.temp[7]-1,
         s=temp_text[7])

plt.text(26,10,"TABLEAU GRAPHIQUE de la temperature en degres du thermometre de Reammur au dessons de Zero",
         fontsize=11)

plt.text(23.25,-14,"Les Cosaque passent au galop \n le Niemen gele.",
         fontsize=11)

plt.savefig("Minard_output.png",
            bbox_inches="tight",
            dpi=500)
plt.show()

# %%
