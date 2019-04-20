import numpy as np

#mat = np.mat([[18,14,0,0],[0,0,18,14],[11,21,0,0],[0,0,11,21]])
#ans = np.array([16,14,25,23])

m1 = np.mat([[18,14],[11,21]])
ans1 = np.array([6,25])


vec = np.linalg.solve(m1,ans1)

print (vec)
#print (np.allclose(np.dot(mat, vec), ans))
