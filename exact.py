import numpy as np
import sympy as sy
m = np.loadtxt('Rosser.txt')
print m
R = sy.Matrix(m)
re = R.eigenvals()
for key in re.keys():
 print '%30s,%5s,\t%f'%(key,re[key],key.evalf())
