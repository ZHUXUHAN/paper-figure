import numpy as np
import matplotlib.pyplot as plt
plt.plot(np.arange(0,20),np.arange(0,20)*np.arange(0,20),'g^-')
plt.plot(np.arange(0,20),np.arange(0,20),'bs-')
plt.plot(np.arange(0,20),np.arange(0,20)*2+1,'ro-')
plt.plot(np.arange(0,20),np.arange(0,20)*8+1,'yx-')

plt.ylabel("c")
plt.legend(['a','b','c','d'])
plt.title('Figure')


plt.savefig("figure.png")
plt.show()
