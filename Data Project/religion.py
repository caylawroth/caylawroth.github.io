import matplotlib.pyplot as plt
import os.path

# Naming the current directory
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'religion_datafile.txt')

datafile = open(filename, 'r',)
data = datafile.readlines()

#Initialize lists
religions = []
religion_labels = ['Buddhist','Christian','Folk Religion','Hindu','Jewish','Other','Shia Muslim','Sunni Muslim','Zoroastrian']

for line in data[1:]:
    country,buddhist,christian,folk,hindu,jewish,other,shia,sunni,zoro = line.split('\t')
    buddhist = int(buddhist)
    christian = int(christian)
    folk = int(folk)
    hindu = int(hindu)
    jewish = int(jewish)
    other = int(other)
    shia = int(shia)
    sunni = int(sunni)
    zoro = int(zoro)
    religions += [buddhist,christian,folk,hindu,jewish,other,shia,sunni,zoro]
    
    fig, ax = plt.subplots(1, 1)
    ax.pie(religions, labels = religion_labels)
    ax.set_title('Citizens of %s by Religion' % country)
    ax.set_aspect(1)
    fig.show()