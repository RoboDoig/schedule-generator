import numpy as np
from sklearn import linear_model

def reward_sequence(n_trials):
    sequence = [0]
    while sum(sequence) != int(n_trials/2):
        # initialise reward vector
        sequence = np.empty(n_trials, dtype=int)
        sequence[0:3] = 1
        sequence[3:6] = 0

        for t in range(6, n_trials):
            preceding_sum = sum(sequence[t-3:t])
            if preceding_sum == 0:
                sequence[t] = 1
            elif preceding_sum == 3:
                sequence[t] = 0
            else:
                sequence[t] = np.random.randint(0, 2)

    return sequence


def generate_correlation_structure(n, rho):
    # remap with corr. structure
    x = np.random.uniform(0.0, 1.0, n).reshape(-1, 1)
    y = np.random.uniform(0.0, 1.0, n).reshape(-1, 1)

    mdl = linear_model.LinearRegression()
    mdl.fit(y, x)

    res = mdl.predict(y) - x

    x = (rho * np.std(res) * y) + (np.sqrt(1 - rho**2) * np.std(y) * res)

    x = (x - np.min(x)) / (np.max(x) - np.min(x))
    y = (y - np.min(y)) / (np.max(y) - np.min(y))

    # get residuals for new correlation structure
    mdl = linear_model.LinearRegression()
    mdl.fit(x, y)

    res = y - mdl.predict(x)

    return x, y, np.hstack(res)
