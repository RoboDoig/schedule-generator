from PyQt5 import QtWidgets
import numpy as np

from Designs import simpleCorrDesign, corrDesign
from Generation import Gen


class SimpleCorrWidget(QtWidgets.QWidget, simpleCorrDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

        self.valence_map = None

    def generate_schedule(self, valence_map):
        lick_fraction = float(self.lickFractionEdit.text())
        n_valves = len(valence_map)

        n_trials = int(self.nTrialsEdit.text())
        n_control_trials = int(self.nControlTrialsEdit.text())
        reward_sequence = Gen.reward_sequence(n_trials + n_control_trials)

        valence_map = np.array(valence_map)
        valve_index = (np.where(valence_map == 0)[0],
                       np.where(valence_map == 1)[0],
                       np.where(valence_map == 2)[0],
                       np.where(valence_map == 3)[0],
                       np.where(valence_map == 4)[0])

        frequency = float(self.pulseFrequencyEdit.text())
        sp_correlated = bool(self.spCorrelatedCheck.isChecked())

        schedule = []
        for t in range(n_trials + n_control_trials):
            # set correlation
            if sp_correlated:
                correlated = True if reward_sequence[t] == 1 else False
            else:
                correlated = False if reward_sequence[t] == 1 else True

            if t < n_trials:
                o1_valve = np.random.choice(valve_index[1], 1) + 1
                o2_valve = np.random.choice(valve_index[2], 1) + 1
                b_valves = np.random.choice(valve_index[0], 2, replace=False) + 1
            else:
                o1_valve = np.random.choice(valve_index[3], 1) + 1
                o2_valve = np.random.choice(valve_index[2], 1) + 1
                b_valves = np.hstack((np.random.choice(valve_index[0], 1)[0] + 1, np.random.choice(valve_index[4], 1)[0] + 1))

            schedule.append([reward_sequence[t], correlated, o1_valve, o2_valve, b_valves, frequency, valence_map,
                             lick_fraction])

        return schedule, ['Rewarded', 'Correlated', 'Odour 1 Valve', 'Odour 2 Valves', 'Blank Valves', 'Frequency',
                          'Valence Map', 'Lick Fraction']

    def pulse_parameters(self, trial):
        params = list()

        onset = float(self.onsetEdit.text())
        offset = float(self.offsetEdit.text())
        length = float(self.trialLengthEdit.text())
        correlated = trial[1]
        o1_valve = trial[2]
        o2_valve = trial[3]
        b_valves = trial[4]
        frequency = trial[5]
        valence_map = trial[6]

        anti_phase_offset = (1.0 / frequency) * 0.5
        phase_choice = np.random.randint(0, 2)

        for p in range(len(valence_map)):
            param = {'type': 'Simple',
                     'fromDuty': True,
                     'frequency': frequency,
                     'duty': 0.5,
                     'fromLength': True,
                     'length': 0.0,
                     'isClean': True,
                     'onset': onset,
                     'offset': offset,
                     'phase_chop': True,
                     'chop_amount': 0.25,
                     'lick_fraction': trial[7]}

            # is this an odour 1 valve
            if p + 1 in o1_valve:
                param['length'] = length
                if correlated:
                    param['onset'] += anti_phase_offset * phase_choice
                else:
                    param['onset'] += anti_phase_offset * phase_choice

            # is this an odour 2 valve
            if p + 1 in o2_valve:
                param['length'] = length
                if correlated:
                    param['onset'] += anti_phase_offset * phase_choice
                else:
                    param['onset'] += anti_phase_offset * (1 - phase_choice)

            # is this a blank valve
            if p + 1 in b_valves:
                param['length'] = length
                if correlated:
                    param['onset'] += anti_phase_offset * (1 - phase_choice)
                else:
                    param['onset'] += anti_phase_offset * np.where(b_valves == p + 1)[0][0]

            params.append(param)

        return params


class CorrWidget(QtWidgets.QWidget, corrDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

        self.valence_map = None

    def generate_schedule(self, valence_map):
        lick_fraction = float(self.lickFractionEdit.text())
        n_valves = len(valence_map)

        n_trials = int(self.nTrialsEdit.text())
        n_control_trials = int(self.nControlTrialsEdit.text())
        reward_sequence = Gen.reward_sequence(n_trials + n_control_trials)

        valence_map = np.array(valence_map)
        valve_index = (np.where(valence_map == 0)[0],
                       np.where(valence_map == 1)[0],
                       np.where(valence_map == 2)[0],
                       np.where(valence_map == 3)[0],
                       np.where(valence_map == 4)[0])

        frequency = float(self.pulseFrequencyEdit.text())
        sp_correlated = bool(self.spCorrelatedCheck.isChecked())

        schedule = []
        for t in range(n_trials + n_control_trials):
            # set correlation
            if sp_correlated:
                correlated = True if reward_sequence[t] == 1 else False
            else:
                correlated = False if reward_sequence[t] == 1 else True

            simple_choice = np.random.uniform() > float(self.fractionSimpleTrialsEdit.text())

            if simple_choice:
                # for a simple choice we will always need 1 o1, 1 o2 valves and 2 b valves all at 50% open
                o1_valve = np.random.choice(valve_index[1], 1, replace=False) + 1
                o1_contributions = [0.5]

                o2_valve = np.random.choice(valve_index[2], 1, replace=False) + 1
                o2_contributions = [0.5]

                b_valve = np.random.choice(valve_index[0], 2, replace=False) + 1
                b_contributions = [0.5, 0.5]
            # otherwise there are some differences according to correlation structure
            else:
                # can be made up of random combination of 1 or 2 valves, b valve contrs. add to 1
                o1_valve = np.random.choice(valve_index[1], np.random.randint(1, 3), replace=False) + 1
                o1_contributions = np.round(np.random.dirichlet(np.ones(len(o1_valve))) * 0.5, 2)

                o2_valve = np.random.choice(valve_index[2], np.random.randint(1, 3), replace=False) + 1
                o2_contributions = np.round(np.random.dirichlet(np.ones(len(o2_valve))) * 0.5, 2)

                if correlated:
                    # if correlated we want our blank valves to add to 1 + we always need 2 valves
                    b_valve = np.random.choice(valve_index[0], 2, replace=False) + 1
                    b_contributions = np.round(np.random.dirichlet(np.ones(len(b_valve))), 2)
                else:
                    # else they must add to 0.5
                    b_valve = np.random.choice(valve_index[0], 2, replace=False) + 1
                    b_contributions = np.round(np.random.dirichlet(np.ones(len(b_valve))) * 0.5, 2)

            schedule.append([reward_sequence[t], correlated, o1_valve, o1_contributions, o2_valve, o2_contributions,
                             b_valve, b_contributions, frequency, valence_map, lick_fraction])

        return schedule, ['Rewarded', 'Correlated', 'Odour 1 Valve', 'O1 Contributions', 'Odour 2 Valves',
                          'O2 Contributions', 'Blank Valves', 'B Contributions', 'Frequency',
                          'Valence Map', 'Lick Fraction']

    def pulse_parameters(self, trial):
        params = list()

        onset = float(self.onsetEdit.text())
        offset = float(self.offsetEdit.text())
        length = float(self.trialLengthEdit.text())
        shatter_hz = float(self.shatterHzEdit.text())
        correlated = trial[1]
        o1_valve = trial[2]
        o1_contr = trial[3]
        o2_valve = trial[4]
        o2_contr = trial[5]
        b_valve = trial[6]
        b_contr = trial[7]
        frequency = trial[8]
        valence_map = trial[9]

        anti_phase_offset = (1.0 / frequency) * 0.5
        phase_choice = np.random.randint(0, 2)

        for p in range(len(valence_map)):
            param = {'type': 'RandomNoise',
                     'fromDuty': True,
                     'frequency': frequency,
                     'duty': 0.5,
                     'fromLength': True,
                     'length': 0.0,
                     'isClean': True,
                     'onset': onset,
                     'offset': offset,
                     'phase_chop': True,
                     'lick_fraction': trial[10],
                     'shadow': False,
                     'shatter_frequency': shatter_hz,
                     'target_duty': 0.5,
                     'amp_min': 0.0,
                     'amp_max': 1.0}

            # is this an odour 1 valve
            if p + 1 in o1_valve:
                param['length'] = length
                param['target_duty'] = o1_contr[np.where(o1_valve == p + 1)[0]]
                if correlated:
                    param['onset'] += anti_phase_offset * phase_choice
                else:
                    param['onset'] += anti_phase_offset * phase_choice

            # is this an odour 2 valve
            if p + 1 in o2_valve:
                param['length'] = length
                param['target_duty'] = o2_contr[np.where(o2_valve == p + 1)[0]]
                if correlated:
                    param['onset'] += anti_phase_offset * phase_choice
                else:
                    param['onset'] += anti_phase_offset * (1 - phase_choice)

            # is this a blank valve
            if p + 1 in b_valve:
                param['length'] = length
                param['target_duty'] = b_contr[np.where(b_valve == p + 1)[0]]
                if correlated:
                    param['onset'] += anti_phase_offset * (1 - phase_choice)
                else:
                    if param['target_duty'] != 0.5:
                        param['shadow'] = True
                    else:
                        param['onset'] += anti_phase_offset * np.where(b_valve == p + 1)[0][0]



            params.append(param)

        return params