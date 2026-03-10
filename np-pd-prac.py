import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Make the array `my_array`
my_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)

# Print `my_array`
#print(my_array)

height = [62, 64, 69, 75, 66,
          68, 65, 71, 76, 73]

weight = [120, 136, 148, 175, 137,
          165, 154, 172, 200, 187]

sns.scatterplot(x=height, y=weight)
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.show()