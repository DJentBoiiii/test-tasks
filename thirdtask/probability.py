import numpy as np
p_H = np.array([0.1, 0.2, 0.4, 0.8, 0.9])
p_m = np.ones(5) / 5
trials = ['H', 'H', 'H', 'T', 'H', 'T', 'H', 'H']
results = []
for trial in trials:
    if trial == 'H':
        p_m = p_H * p_m
    else:
        p_m = (1 - p_H) * p_m
    p_m /= p_m.sum()
    p_next_H = (p_H * p_m).sum()
    results.append(p_next_H)
print([round(i, 2) for  i in results])
