from PyQt5 import QtWidgets
import numpy as np

from Designs import basicGNGDesign
from Generation import Gen


class BasicGNGWidget(QtWidgets.QWidget, basicGNGDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

    def generate_schedule(self, valence_map):
        # how many valves available
        n_valves = len(valence_map)

        # generate the reward sequence
        n_trials = int(self.nTrialsEdit.text())
        reward_sequence = Gen.reward_sequence(n_trials)

        # for each trial, pick a random valve of the correct valence to use
        valence_map = np.array(valence_map)
        valve_index = (np.where(valence_map == 0)[0], np.where(valence_map == 1)[0])

        schedule = []
        for t in range(n_trials):
            valve_choices = valve_index[reward_sequence[t]]
            valve = np.random.choice(valve_choices)
            schedule.append([reward_sequence[t], valve])

        return schedule, ['reward_sequence', 'valve']



