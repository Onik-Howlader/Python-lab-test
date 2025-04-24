import numpy as np

a = [
    [[1, 2], [1, 2], [2, 4]],
    [[1, 2], [1, 2], [3, 4]]
]

a = np.array(a)
print (a.shape)
print(a[0, 2])