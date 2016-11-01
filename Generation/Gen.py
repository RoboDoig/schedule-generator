import numpy as np


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

print(sum(reward_sequence(12)))