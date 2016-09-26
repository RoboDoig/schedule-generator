from PyQt5 import QtWidgets
import numpy as np

from Designs import basicGNGDesign
from Generation import Gen


class BasicGNGWidget(QtWidgets.QWidget, basicGNGDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

        self.valence_map = None

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
            valve = np.random.choice(valve_choices) + 1
            schedule.append([reward_sequence[t], valve, valence_map])

        return schedule, ['reward_sequence', 'valve', 'valence_map']

    def pulse_parameters(self, trial):
        params = list()
        valence_map = trial[2]

        onset = float(self.onsetEdit.text())
        offset = float(self.offsetEdit.text())
        length = float(self.trialLengthEdit.text())

        for p in range(len(valence_map)):

            param = {'type': 'Simple',
                     'fromDuty': False,
                     'fromValues': True,
                     'pulse_width': length,
                     'pulse_delay': 0.0,
                     'fromLength': False,
                     'fromRepeats': True,
                     'repeats': 1,
                     'isClean': True,
                     'isShatter': False,
                     'onset': onset,
                     'offset': offset}

            if p != trial[1]-1:
                param['repeats'] = 0

            params.append(param)

        return params


