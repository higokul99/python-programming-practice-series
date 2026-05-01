import numpy as np

n1 = np.array([10,20,30,4,50,60])
print(np.mean(n1))
print(np.median(n1))
print(np.std(n1))


c1 = np.array([10,20,30])
c2 = np.array([30,40,50])

print(np.vstack((c1,c2)))