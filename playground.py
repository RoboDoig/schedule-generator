import numpy as np
from Generation import Gen as gen
import matplotlib.pyplot as plt
import scipy.stats as stats

x, y, res = gen.generate_correlation_structure(10, 0.9)

c = stats.pearsonr(x, y)
print(c)
print(res)

plt.scatter(x, y)
plt.show()



