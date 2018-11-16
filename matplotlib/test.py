import numpy as np
import matplotlib.pyplot as plt


N = 10
x = np.random.randint(0,10,N)
y = np.random.randint(0,10,N)

print(x)
print(y)

color = np.add(x,y)
#plt.figure(figsize=(10,10))
plt.scatter(x, y,c=color,alpha=0.5)
plt.show()








