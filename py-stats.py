from scipy.stats import uniform

min_time = 0
max_time = 30

# calculating probability of waiting less than 5 minutes
prob_waiting_less_than_5 = uniform.cdf(5, min_time, max_time)
print("Probability of waiting less than 5 minutes:", prob_waiting_less_than_5)

# calculating probability of waiting more than 5 minutes
prob_waiting_more_than_5 = 1 - prob_waiting_less_than_5
print("Probability of waiting more than 5 minutes:", prob_waiting_more_than_5)