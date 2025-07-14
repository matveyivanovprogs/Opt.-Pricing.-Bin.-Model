import numpy as np
import matplotlib as plt
def choose(k, n):
    a=1
    for i in range(k):
        a*=(n-i)/(i+1)
    return a
#Calculate Risk Neutral Probabilities
def q_up(u, d, interest_rate, time):
    interest=exp(interest_rate*time)
    assert u > interest and d< interest, "By NA condition"
    return (u-interest)/(u-d)
def q_down():
    return 1-martingale_up()
