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
                       np.where(valence_map == 2)[0],
                       np.where(valence_map == 3)[0],
                       np.where(valence_map == 4)[0])

        onset = float(self.onsetEdit.text())
        offset = float(self.onsetEdit.text())
        length = float(self.trialLengthEdit.text())
        pulse_hz = float(self.pulseFrequencyEdit.text())
        shatter_hz = float(self.shatterFrequencyEdit.text())
        shatter_duty_min = float(self.shatterDutyMinEdit.text())
        shatter_duty_max = float(self.shatterDutyMaxEdit.text())
        nControlTrial = int(self.nControlTrialsEdit.text())
        single_valve_trials = float(self.fractionSingleValveEdit.text())
        sp_correlated = bool(self.spCorrelatedCheck.isChecked())

        # algorithm to pick trials
        schedule = []
        for t in range(n_trials):
            # decide whether odours are correlated or anti-correlated based on reward settings
            if sp_correlated:
                correlated = True if reward_sequence[t] == 1 else False
            if not sp_correlated:
                correlated = False if reward_sequence[t] == 1 else True

            # decide whether single or multi-valve trial
            v_decision = np.random.uniform()
            if v_decision <= single_valve_trials:
                # single_valve_trial
                b_valves = np.random.choice(valve_index[0], 1, replace=False) + 1
                o1_valves = np.random.choice(valve_index[1], 1) + 1
                o2_valves = np.random.choice(valve_index[2], 1) + 1

            else:
                # multi valve trial
                b_valves = np.random.choice(valve_index[0], np.random.randint(1, 3), replace=False) + 1
                o1_valves = np.random.choice(valve_index[1], np.random.randint(1, 3), replace=False) + 1
                o2_valves = np.random.choice(valve_index[2], np.random.randint(1, 3), replace=False) + 1

            # choose relative contributions based on whether trial is correlated or not
            o1_contribution = np.round(np.random.dirichlet(np.ones(len(o1_valves))) / 4.0, 2)
            o2_contribution = np.round(np.random.dirichlet(np.ones(len(o2_valves))) / 4.0, 2)

            if correlated:
                b_contribution = np.round(np.random.dirichlet(np.ones(len(b_valves))) / 2.0, 2)
            else:
                b_contribution = [0.5 - sum(o1_contribution), 0.5 - sum(o2_contribution)]

            schedule.append([reward_sequence[t], correlated, b_valves, b_contribution, o1_valves, o1_contribution,
                             o2_valves, o2_contribution, pulse_hz, length, valence_map])

        return schedule, ['Rewarded', 'Correlated', 'Blank Vales', 'Blank Contribution', 'Odour 1 Valves',
                          'Odour 1 Contribution', 'Odour 2 Valves', 'Odour 2 Contribution', 'Hz', 'Length',
                          'Valence Map']

    def pulse_parameters(self, trial):
        valence_map = trial[10]
        params = list()

        onset = float(self.onsetEdit.text())
        offset = float(self.offsetEdit.text())
        length = float(self.trialLengthEdit.text())
        shatter_frequency = float(self.shatterFrequencyEdit.text())
        amp_min = float(self.shatterDutyMinEdit.text())
        amp_max = float(self.shatterDutyMaxEdit.text())

        # compiled_valves = [item for sublist in [trial[2], trial[4], trial[6]] for item in sublist]
        # compiled_contributions = [np.round(item, 2) for sublist in [trial[3], trial[5], trial[7]] for item in sublist]

        for p in range(len(valence_map)):
            param = {'type': 'RandomNoise',
                     'fromDuty': True,
                     'fromValues': False,
                     'frequency': trial[8],
                     'duty': 0.5,
                     'fromLength': True,
                     'fromRepeats': False,
                     'length': 0.0,
                     'isClean': False,
                     'isShatter': True,
                     'shatter_frequency': shatter_frequency,
                     'target_duty': 0.5,
                     'onset': onset,
                     'offset': offset,
                     'amp_min': amp_min,
                     'amp_max': amp_max}

            # place odour 1
            if p + 1 in trial[4]:
                param['length'] = length
                param['target_duty'] = trial[5][np.where(trial[4] == p + 1)[0]]

            # place odour 2
            if p + 1 in trial[6]:
                param['length'] = length
                if not trial[1]:
                    param['onset'] = onset + ((1.0 / trial[8])/2.0)

            # place blanks
            if p + 1 in trial[2]:
                param['length'] = length
                if trial[1]:
                    param['onset'] = onset + ((1.0 / trial[8])/2.0)
                else:
                    param['onset'] = onset + (np.where(trial[2] == p + 1)[0][0] * ((1.0 / trial[8]) / 2.0))

            params.append(param)

        return params
