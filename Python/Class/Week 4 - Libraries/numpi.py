#pip install --upgrade --force-reinstall numpy

import numpy as np 
# Creating an array using np.array() method 
arr = np.array([10, 20, 30, 40, 50]) 
# Printing 
print(arr)

# more than one dimensions 
import numpy as np 
a = np.array([[1, 2], [3, 4], [5,6], [8,7], [9,10]]) 
print(a)

# minimum dimensions 
import numpy as np 
a = np.array([1, 2, 3, 4, 5], ndmin = 2) 
print(a)

# dtype parameter 
import numpy as np 
a = np.array([1, 2, 3], dtype = complex) 
print(a)

# dtype parameter 
import numpy as np 
a = np.array([1, 2, 3], dtype = bool) 
print(a)