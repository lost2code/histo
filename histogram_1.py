import random
from matplotlib import pyplot as plt

#A dataset of 100 people in age group 1 to 100

#data = []
#for i in range(100):
#    data.append(random.randint(1,100)
#or
data = [random.randint(1,100) for i in range(100) ]

#read it
print(data)

#Plot a Histogram
#i.e.
#Distribute the dataset ranging 1-100 into 10 intervals (bins). 
#The 10 bins represents number of people in age groups 1-10, 11-20, ..., 91-100

#plt.hist(data, bins, range)
plt.hist(x = data, bins = 10, range = (1,100))

plt.show()

#A histogram is a representation of distribution of values of a dataset.