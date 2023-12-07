#Import packages, set wd, & download dataframe
#I will be using matplotlib
import os
#os.chdir("D:\\School\\Spring 2023\\Data Vis")
import matplotlib.pyplot as plt
import pandas
import pandas as pd
from matplotlib import pyplot
import seaborn

ferry_url = "https://data.cityofnewyork.us/resource/t5n6-gx8c.csv?$select=date,route,SUM(boardings)&$group=date,route&$limit=1000000"
ferry = pandas.read_csv(ferry_url)
#%%
ferry.summarize()
#%%
#>I reorder the categories using Pandas so that they render as in order
#as close as possible to bringing the smallest curves to the front,
#and sending the largest ones to the back. Otherwise, some curves
#would render hidden behind others.

ferry['route'] = pd.Categorical(ferry["route"], categories = ["ER","RW","SB","AS","SV","GI","RR","LE","SG"], ordered=True)

#%%
#>I reduce the alpha to further improve readability.
#>The final graph comes out clearer, and with apparently
#higher alpha as a png using plt.savefig()
#than it does in the output console.
seaborn.lineplot(data=ferry, x="date", y="SUM_boardings", hue="route",
                 linewidth=1, alpha=0.5)

#>I change axis titles & add a graph title to make the graph
#clearer and more polished for a general audience.
plt.xlabel("Date of Trip")
plt.ylabel("Total Boardings")
plt.title("Ferry Boardings by Date", fontsize= 14)

#>I set the x-axis ticks as close to accurate as possible, but the x axis tics seem to render
#on a non-constant scale. That is, 2018, 2020, & 2021 do not appear equidistant when all are rendered.
#After some trial-and-error I couldn't uncover what is causing this, or how to fix this. So this is
#the onecriticism that I couldn't seem to fix, only work around. I also suspect having a tic for every
#year may create somewhat too high information density.
plt.xticks(ticks=["2017-07-01T00:00:00.000","2019-07-01T00:00:00.000","2022-07-01T00:00:00.000"], labels=["2017","2019","2022"])

#>I output the file at 300 dpi to produce a clearer graph than the default resolution.
plt.savefig("ferry_graph.png", dpi=300)
plt.show()

#I think it is still somewhat difficult to differentiate between each group's curve
#If I had more time & expertise, I think it would be a good idea to make this plot
#interactive where by hovering/clicking the mouse on a given group in the legend, you
#can raise the alpha of that group's curve and reduce the alpha of all other groups'
#curves to inspect the desiered curve.
#%%
