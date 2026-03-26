# central limit theorem example with a die
import numpy as np

die = np.array([1, 2, 3, 4, 5, 6])
sample_mean = []

for i in range(10):
    sample_5 = np.random.choice(die, size=5, replace=True)
    sample_mean.append(sample_5.mean())
print("Sample means:", sample_mean)

"""
To review all other types of statitical measures like normal distribution, standard deviation, variance, 
poison distribution, binomial distribution, normal distribution, uniform distribution, discrete distribution, continuous distribution, probability density function, cumulative distribution function, z-scores, t-scores, confidence intervals, hypothesis testing, p-values, correlation coefficient, regression analysis, 
and how to calculate them using scipy.stats module, and also how to visualize them using matplotlib.pyplot module.

"""