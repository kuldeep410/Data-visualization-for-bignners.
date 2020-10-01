import pandas as pd
from matplotlib import pyplot as plt
fruit = ['Apple','Mango','Guava','Orange','PineApple']
quantity = [10,5,15,20,8]
plt.pie(quantity,labels=fruit,autopct='%0.1f',colors=['yellow','blue','green','red','orange'])
plt.show()
plt.pie(quantity,labels=fruit,radius = 2,autopct='%0.1f%%',colors=['yellow','blue','green','red','orange'])
plt.pie([50],radius=1,colors=['w'])
plt.show()