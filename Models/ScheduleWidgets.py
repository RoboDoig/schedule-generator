from PyQt5 import QtWidgets
import numpy as np

from Designs import basicGNGDesign, v8CorrDesign
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

        # get necessary parameters
        valence_map = np.array(valence_map)
        valve_index = (np.where(valence_map == 0)[0], np.where(valence_map == 1)[0])

        onset = float(self.onsetEdit.text())
        offset = float(self.onsetEdit.text())
        length = float(self.trialLengthEdit.text())

        schedule = []
        for t in range(n_trials):
            valve_choices = valve_index[reward_sequence[t]]
            valve = np.random.choice(valve_choices) + 1
            schedule.append([reward_sequence[t], valve, onset, offset, length, valence_map])

        return schedule, ['reward_sequence', 'valve', 'onset', 'offset', 'length', 'valence_map']

    def pulse_parameters(self, trial):
        params = list()
        valence_map = trial[5]

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


class V8CorrWidget(QtWidgets.QWidget, v8CorrDesign.Ui_Form):
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

        # get necessary calculation parameters
        valence_map = np.array(valence_map)
        valve_index = (np.where(valence_map == 0)[0],
                       np.where(valence_map == 1)[0],
                       np.where(valence_map == 2)[0])

        onset = float(self.onsetEdit.text())
        offset = float(self.onsetEdit.text())
        length = float(self.trialLengthEdit.text())
        pulse_hz = float(self.pulseFrequencyEdit.text())
        shatter_hz = float(self.shatterFrequencyEdit.text())
        shatter_duty_min = float(self.shatterDutyMinEdit.text())
        shatter_duty_max = float(self.shatterDutyMaxEdit.text())
        nControlTrial = int(self.nControlTrialsEdit.text())
        single_valve_trials = float(self.fractionSingleValveEdit.text())
        sp_correlated = bool(self.spCorrelatedEdit.text())

        # algorithm to pick trials
        schedule = []
        for t in range(n_trials):
            # decide whether single or multi-valve trial
            v_decision = np.random.uniform()
            if v_decision <= single_valve_trials:
                # single_valve_trial
                b_valves = np.random.choice(valve_index[0], 2, replace=False) + 1
                o1_valve = np.random.choice(valve_index[1], 1) + 1
                o2_valve = np.random.choice(valve_index[2], 1) + 1