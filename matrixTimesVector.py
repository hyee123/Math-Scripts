import numpy as np

mat = [[12,11],[3,2]]
mat = np.matrix(mat)
vec = [18,14]
vec = np.array(vec)

ans = mat.dot(vec)
i = 0
while i < len(ans):
    ans[i] = ans[i] % 26
    i += 1
print (ans)
