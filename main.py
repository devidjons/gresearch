import numpy as np
import pandas as pd
import sympy as sp
import pdb
import matplotlib.pyplot as plt
import itertools as it
import scipy


def prob(x, N = 10000):
	sample = []
	for i in range(N):
		sum = 0
		while sum <= x:
			sum += np.random.uniform(0, 1, 1)
		if sum > 1:
			sample.append(0)
		else:
			sample.append(1)
	return np.mean(sample)

xs = np.linspace(0,1,num = 100000)
ps = np.array([prob(x) for x in xs])