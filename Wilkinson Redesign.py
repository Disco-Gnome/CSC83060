import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

os.chdir("D:\\School\\Spring 2023\\Data Vis\\Redesign Wilkinson")

bibledtype = pd.api.types.CategoricalDtype(categories=[
    '(1) WORD OF GOD',
    '(2) INSPIRED WORD',
    '(3) BOOK OF FABLES',
    '(4) OTHER'], ordered=True)
partnersdtype = pd.api.types.CategoricalDtype(categories=['0', '1', '2', '3', '4', '5-10', '11-20', '21-100'], ordered=True)
data = pd.read_csv("sexbiblecounts.csv")
data["bible"] = data["bible"].astype(bibledtype)
data["partners"] = data["partners"].astype(partnersdtype)

del(bibledtype, partnersdtype)

piv = data.pivot("partners","bible","count")
piv = piv.drop("(4) OTHER",
               axis=1)

for j in range(len(piv.columns)):
    for i in (range(len(piv))):
        piv.iloc[i,j] = 100 * piv.iloc[i,j] / np.nansum(piv.iloc[:,j])

piv = piv.fillna(0)
piv.index = [0,1,2,3,4,5,6,7]
piv["partners"] = ["0","1","2","3","4","5-10","11-20","21-100"]
#%%
font = {'family': 'Verdana',
        'weight': 'normal',
        'size': 8}
mpl.rc('font', **font)

plt.figure(facecolor="#EFE4D2")
plt.axes().set_facecolor("#EFE4D2")
plt.plot(piv["partners"],
         piv["(1) WORD OF GOD"],
         color="#1B5E20")
plt.plot(piv["partners"],
         piv["(2) INSPIRED WORD"],
         color="#43A047")
plt.plot(piv["partners"],
         piv["(3) BOOK OF FABLES"],
         color="#81C784")
plt.legend(piv,
           title="The Bible is...",
           labels=("The word of God", "Inspired word", "A book of fables"),
           bbox_to_anchor=(0.3, 0.2,0.0,0.0),
           framealpha=0.75,
           facecolor="#EFE4D2",
           edgecolor="#EFE4D2")
plt.yticks([10,20,30,40,50,60,70,80,90])
plt.margins(x=0)
plt.ylim(0,100)
plt.yticks([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
           ["","10%","","20%","","30%","","40%","","50%","","60%","","70%","","80%","","90%","","100%"],
           fontsize=6)
plt.xticks(["1","2","3","4","5-10","11-20","21-100"],
           ["1","2","3","4","5 - 10","11 - 20","21 - 100"],
           fontsize=6)
plt.text(-0.1,-3.5,"0")
plt.xlabel("Number of Sexual Partners in the Past Year")
plt.ylabel("Proportion of Respondents")
plt.grid(axis="y")

plt.suptitle("Number of Sexual Partners by Religiosity",
             fontsize=14)

ax = plt.subplot(111)
ax.spines[['right', 'top']].set_visible(False)


plt.savefig("Wilkinson Redesign.png",
            dpi=300)
plt.show()


