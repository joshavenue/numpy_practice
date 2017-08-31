import numpy as np
import random

x1 = int(input('Num 1 : '))
y1 = int(input('Num 2 : '))
z1 = int(input('Num 3 : '))

x2 = int(input('Num 1 : '))
y2 = int(input('Num 2 : '))
z2 = int(input('Num 3 : '))

xyz = np.array([x1,y1,z1])
xyz2 = np.array([[x2],[y2],[z2]])
xyz3 = np.dot(xyz,xyz2)

print(xyz)
print(xyz2)
print(xyz3)
