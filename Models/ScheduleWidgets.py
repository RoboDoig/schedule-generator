from PyQt5 import QtWidgets
import numpy as np
import random

from Designs import simpleCorrDesign, corrDesign, simpleGNGDesign, pretrainDesign, shatterValveTestDesign, \
    corrRandomFrequencyDesign, corrRandomFrequency2Design, corrDifficultySwitchDesign, corrOnsetDisruptDesign, \
    concGNGDesign, corrDifficultySwitchCameraTriggerDesign, contCorrDesign
from Generation import Gen


class PretrainWidget(QtWidgets.QWidget, pretrainDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

        self.valence_map = None

    def generate_schedule(self, valence_map):
        lick_fraction = float(self.lickFractionEdit.text())
        n_valves = len(valence_map)

        n_trials = int(self.nTrialsEdit.text())
        target = int(self.targetEdit.text())

        valence_map = np.array(valence_map)
        valve_index = (np.where(valence_map == 0)[0],
                       np.where(valence_map == 1)[0],
                       np.where(valence_map == 2)[0],
                       np.where(valence_map == 3)[0],
                       np.where(valence_map == 4)[0])

        schedule = []
        for t in range(n_trials):
            valve = np.random.choice(valve_index[target], 1) + 1
            schedule.append([1, valve, valence_map, lick_fraction])

        return schedule, ['Rewarded', 'Valve', 'Valence Map', 'Lick Fraction']

    def pulse_parameters(self, trial):
        params = list()

        onset = float(self.onsetEdit.text())
        offset = float(self.offsetEdit.text())
        length = float(self.trialLengthEdit.text())
        valve = trial[1]
        valence_map = trial[2]

        for p in range(len(valence_map)):
            param = {'type': 'Simple',
                     'fromDuty': False,
                     'fromValues': True,
                     'pulse_width': length,
                     'pulse_delay': 0.0,
                     'fromLength': False,
                     'fromRepeats': True,
                     'repeats': 0,
                     'length': 0.0,
                     'isClean': True,
                     'onset': onset,
                     'offset': offset,
                     'lick_fraction': trial[3]}

            if p + 1 in valve:
                param['repeats'] = 1

            params.append(param)

        return params


class ConcGNGWidget(QtWidgets.QWidget, concGNGDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

        self.valence_map = None

    def generate_schedule(self, valence_map):
        lick_fraction = float(self.lickFractionEdit.text())
        n_valves = len(valence_map)
        min_conc = float(self.minConcEdit.text())

        n_trials = int(self.nTrialsEdit.text())
        reward_sequence = Gen.reward_sequence(n_trials)

        valence_map = np.array(valence_map)
        valve_index = (np.where(valence_map == 0)[0],
                       np.where(valence_map == 1)[0],
                       np.where(valence_map == 2)[0])

        if not bool(self.reverseValenceCheck.isChecked()):
            rewarded_choice = valve_index[1]
            unrewarded_choice = valve_index[2]
        else:
            rewarded_choice = valve_index[2]
            unrewarded_choice = valve_index[1]

        schedule = []
        for t in range(n_trials):
            rewarded = reward_sequence[t] == 1

            if rewarded:
                valve = np.random.choice(rewarded_choice, 1) + 1
            else:
                valve = np.random.choice(unrewarded_choice, 1) + 1

            conc_level = np.round(np.random.uniform(min_conc, 1.0), 2)

            schedule.append([reward_sequence[t], valve, valence_map, conc_level, lick_fraction])

        return schedule, ['Rewarded', 'Valve', 'Valence Map', 'Conc. Level', 'Lick Fraction']

    def pulse_parameters(self, trial):
        params = list()

        onset = float(self.onsetEdit.text())
        offset = float(self.offsetEdit.text())
        length = float(self.trialLengthEdit.text())

        valve = trial[1]
        valence_map = trial[2]
        conc_level = trial[3]

        for p in range(len(valence_map)):
            param = {'type': 'Simple',
                     'fromDuty': False,
                     'fromValues': True,
                     'pulse_width': length,
                     'pulse_delay': 0.0,
                     'fromLength': False,
                     'fromRepeats': True,
                     'repeats': 0,
                     'length': 0.0,
                     'isClean': False,
                     'isShatter': True,
                     'shatter_frequency': 500.0,
                     'shatter_duty': conc_level,
                     'onset': onset,
                     'offset': offset,
                     'lick_fraction': trial[3]}

            if p + 1 in valve:
                param['repeats'] = 1

            params.append(param)

        return params


class SimpleGNGWidget(QtWidgets.QWidget, simpleGNGDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

        self.valence_map = None

    def generate_schedule(self, valence_map):
        lick_fraction = float(self.lickFractionEdit.text())
        n_valves = len(valence_map)

        n_trials = int(self.nTrialsEdit.text())
        reward_sequence = Gen.reward_sequence(n_trials)

        valence_map = np.array(valence_map)
        valve_index = (np.where(valence_map == 0)[0],
                       np.where(valence_map == 1)[0],
                       np.where(valence_map == 2)[0],
                       np.where(valence_map == 3)[0],
                       np.where(valence_map == 4)[0])

        if not bool(self.reverseValenceCheck.isChecked()):
            rewarded_choice = valve_index[1]
            unrewarded_choice = valve_index[2]
        else:
            rewarded_choice = valve_index[2]
            unrewarded_choice = valve_index[1]

        schedule = []
        for t in range(n_trials):
            rewarded = reward_sequence[t] == 1

            if rewarded:
                valve = np.random.choice(rewarded_choice, 1) + 1
            else:
                valve = np.random.choice(unrewarded_choice, 1) + 1

            schedule.append([reward_sequence[t], valve, valence_map, lick_fraction])

        return schedule, ['Rewarded', 'Valve', 'Valence Map', 'Lick Fraction']

    def pulse_parameters(self, trial):
        params = list()

        onset = float(self.onsetEdit.text())
        offset = float(self.offsetEdit.text())
        length = float(self.trialLengthEdit.text())
        valve = trial[1]
        valence_map = trial[2]

        for p in range(len(valence_map)):
            param = {'type': 'Simple',
                     'fromDuty': False,
                     'fromValues': True,
                     'pulse_width': length,
                     'pulse_delay': 0.0,
                     'fromLength': False,
                     'fromRepeats': True,
                     'repeats': 0,
                     'length': 0.0,
                     'isClean': True,
                     'onset': onset,
                     'offset': offset,
                     'lick_fraction': trial[3]}

            if p + 1 in valve:
                param['repeats'] = 1

            params.append(param)

        return params


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

            if t < n_trials:
                o1_choice = valve_index[1]
                o2_choice = valve_index[2]
                b_choice = valve_index[0]
            else:
                simple_choice = True
                o1_choice = valve_index[3]
                o2_choice = valve_index[2]
                b_choice = np.hstack((valve_index[4], np.random.choice(valve_index[0], 1)))

            if simple_choice:
                # for a simple choice we will always need 1 o1, 1 o2 valves and 2 b valves all at 50% open
                o1_valve = np.random.choice(o1_choice, 1, replace=False) + 1
                o1_contributions = [0.5]

                o2_valve = np.random.choice(o2_choice, 1, replace=False) + 1
                o2_contributions = [0.5]

                b_valve = np.random.choice(b_choice, 2, replace=False) + 1
                b_contributions = [0.5, 0.5]
            # otherwise there are some differences according to correlation structure
            else:
                # can be made up of random combination of 1 or 2 valves, b valve contrs. add to 1
                o1_valve = np.random.choice(o1_choice, np.random.randint(1, len(o1_choice) + 1), replace=False) + 1
                o1_contributions = np.round(np.random.dirichlet(np.ones(len(o1_valve))) * 0.5, 2)

                o2_valve = np.random.choice(o2_choice, np.random.randint(1, 3), replace=False) + 1
                o2_contributions = np.round(np.random.dirichlet(np.ones(len(o2_valve))) * 0.5, 2)

                if correlated:
                    # if correlated we want our blank valves to add to 1 + we always need 2 valves
                    b_valve = np.random.choice(b_choice, 2, replace=False) + 1

                    b_contributions = np.array([1.0, 0.0])
                    while np.prod(b_contributions) == 0:
                        b_contributions = np.round(np.random.dirichlet(np.ones(len(b_valve))), 2)
                else:
                    # else they must add to 0.5
                    b_valve = np.random.choice(b_choice, 2, replace=False) + 1

                    b_contributions = np.array([1.0, 0.0])
                    while np.prod(b_contributions) == 0:
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


class ContCorrWidget(QtWidgets.QWidget, contCorrDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

        self.valence_map = None

    def generate_schedule(self, valence_map):
        lick_fraction = float(self.lickFractionEdit.text())
        n_valves = len(valence_map)

        n_trials = int(self.nTrialsEdit.text())
        reward_sequence = Gen.reward_sequence(n_trials)

        valence_map = np.array(valence_map)
        valve_index = (np.where(valence_map == 0)[0],
                       np.where(valence_map == 1)[0],
                       np.where(valence_map == 2)[0])

        frequency = float(self.pulseFrequencyEdit.text())
        sp_correlated = bool(self.spCorrelatedCheck.isChecked())

        schedule = []
        for t in range(n_trials):
            # set correlation
            if sp_correlated:
                correlated = True if reward_sequence[t] == 1 else False
            else:
                correlated = False if reward_sequence[t] == 1 else True

            # choose rho - TODO for now set to 1 for corr, 0 for uncorr
            if correlated:
                # rho = np.round(np.random.uniform(0, 1.0), 1)
                rho = 1.0
            else:
                # rho = np.round(np.random.uniform(-1.0, 0.0), 1)
                rho = 0.0

            simple_choice = np.random.uniform() > float(self.fractionSimpleTrialsEdit.text())

            o1_choice = valve_index[1]
            o2_choice = valve_index[2]
            b_choice = valve_index[0]

            if simple_choice:
                # for a simple choice we will always need 1 o1, 1 o2 valves and 2 b valves all at 50% open
                o1_valve = np.random.choice(o1_choice, 1, replace=False) + 1
                o1_contributions = [0.5]

                o2_valve = np.random.choice(o2_choice, 1, replace=False) + 1
                o2_contributions = [0.5]

                b_valve = np.random.choice(b_choice, 2, replace=False) + 1
                b_contributions = [0.5, 0.5]
            # otherwise there are some differences according to correlation structure
            else:
                # can be made up of random combination of 1 or 2 valves, b valve contrs. add to 1
                o1_valve = np.random.choice(o1_choice, np.random.randint(1, len(o1_choice) + 1), replace=False) + 1
                o1_contributions = np.round(np.random.dirichlet(np.ones(len(o1_valve))) * 0.5, 2)

                o2_valve = np.random.choice(o2_choice, np.random.randint(1, 3), replace=False) + 1
                o2_contributions = np.round(np.random.dirichlet(np.ones(len(o2_valve))) * 0.5, 2)

                b_valve = np.random.choice(b_choice, 2, replace=False) + 1
                b_contributions = [0.5, 0.5]

            schedule.append([reward_sequence[t], correlated, o1_valve, o1_contributions, o2_valve, o2_contributions,
                             b_valve, b_contributions, frequency, valence_map, lick_fraction, rho])

        return schedule, ['Rewarded', 'Correlated', 'Odour 1 Valve', 'O1 Contributions', 'Odour 2 Valves',
                          'O2 Contributions', 'Blank Valves', 'B Contributions', 'Frequency',
                          'Valence Map', 'Lick Fraction', 'Rho']

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
        rho = trial[11]

        anti_phase_offset = (1.0 / frequency) * 0.5
        phase_choice = np.random.randint(0, 2)
        straight_choice = np.random.randint(0, 2)

        x, y, res = Gen.generate_correlation_structure(1000, rho)
        n = int(length * frequency)
        y_mod = np.random.choice(res, n) * (1.0 / frequency)

        for p in range(len(valence_map)):
            param = {'type': 'ContCorr',
                     'frequency': frequency,
                     'pulse_length': (1.0 / frequency) / 2.0,
                     'amp_min': 0.0,
                     'amp_max': 1.0,
                     'shatter_frequency': shatter_hz,
                     'onset': onset,
                     'offset': offset,
                     'pulse_times': [],
                     'target_duty': 0.5,
                     'invert': False,
                     'reverse': False,
                     'lick_fraction': trial[10]}

            if straight_choice is 1:
                o1_times = np.linspace(0, length, length * frequency, endpoint=False)
                o2_times = np.linspace(0, length, length * frequency, endpoint=False) + y_mod
            else:
                o1_times = np.linspace(0, length, length * frequency, endpoint=False) + y_mod
                o2_times = np.linspace(0, length, length * frequency, endpoint=False)

            if not correlated:
                if phase_choice is 0:
                    o2_times += (1.0 / frequency) / 2.0
                else:
                    o1_times += (1.0 / frequency) / 2.0

            if correlated and phase_choice is 1:
                param['reverse'] = True

            comb = [o1_times, o2_times]

            # is this an odour 1 valve
            if p + 1 in o1_valve:
                param['pulse_times'] = o1_times
                param['target_duty'] = o1_contr[int(np.where(o1_valve == p + 1)[0])]

            # is this an odour 2 valve
            if p + 1 in o2_valve:
                param['pulse_times'] = o2_times
                param['target_duty'] = o2_contr[int(np.where(o2_valve == p + 1)[0])]

            # is this a blank valve
            if p + 1 in b_valve:
                param['invert'] = True
                param['pulse_times'] = comb[int(np.where(b_valve == p + 1)[0][0])]
                param['target_duty'] = b_contr[int(np.where(b_valve == p + 1)[0])]
                # if correlated:
                #     param['onset'] += anti_phase_offset * phase_choice
                #     print(phase_choice)
                # else:
                #     print('placeholder')
                #     param['onset'] += anti_phase_offset * (np.where(b_valve == p + 1)[0][0] * (1 - phase_choice))

            params.append(param)

        return params


class CorrOnsetDisruptWidget(QtWidgets.QWidget, corrOnsetDisruptDesign.Ui_Form):
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
        ctrl_trials = random.sample(range(0, n_trials),n_control_trials)
        for t in range(n_trials):
            # set correlation
            if sp_correlated:
                correlated = True if reward_sequence[t] == 1 else False
            else:
                correlated = False if reward_sequence[t] == 1 else True

            simple_choice = np.random.uniform() > float(self.fractionSimpleTrialsEdit.text())

            if t < n_trials:
                o1_choice = valve_index[1]
                o2_choice = valve_index[2]
                b_choice = valve_index[0]
            else:
                simple_choice = True
                o1_choice = valve_index[3]
                o2_choice = valve_index[2]
                b_choice = np.hstack((valve_index[4], np.random.choice(valve_index[0], 1)))

            if simple_choice:
                # for a simple choice we will always need 1 o1, 1 o2 valves and 2 b valves all at 50% open
                o1_valve = np.random.choice(o1_choice, 1, replace=False) + 1
                o1_contributions = [0.5]

                o2_valve = np.random.choice(o2_choice, 1, replace=False) + 1
                o2_contributions = [0.5]

                b_valve = np.random.choice(b_choice, 2, replace=False) + 1
                b_contributions = [0.5, 0.5]
            # otherwise there are some differences according to correlation structure
            else:
                # can be made up of random combination of 1 or 2 valves, b valve contrs. add to 1
                o1_valve = np.random.choice(o1_choice, np.random.randint(1, len(o1_choice) + 1), replace=False) + 1
                o1_contributions = np.round(np.random.dirichlet(np.ones(len(o1_valve))) * 0.5, 2)

                o2_valve = np.random.choice(o2_choice, np.random.randint(1, 3), replace=False) + 1
                o2_contributions = np.round(np.random.dirichlet(np.ones(len(o2_valve))) * 0.5, 2)

                if correlated:
                    # if correlated we want our blank valves to add to 1 + we always need 2 valves
                    b_valve = np.random.choice(b_choice, 2, replace=False) + 1

                    b_contributions = np.array([0.5, 0.5])
                else:
                    # else they must add to 0.5
                    b_valve = np.random.choice(b_choice, 2, replace=False) + 1

                    b_contributions = np.array([0.25, 0.25])

            if reward_sequence[t] > 0.5:
                if np.random.uniform(0.0, 1.0) > float(self.fractionSpRewardedEdit.text()):
                    reward_sequence[t] = 0

            if t in ctrl_trials:
                ctrl_trial = 1
            else:
                ctrl_trial = 0

            schedule.append([reward_sequence[t], correlated, o1_valve, o1_contributions, o2_valve, o2_contributions,
                             b_valve, b_contributions, frequency, valence_map, lick_fraction, np.random.randint(0, 2),
                             np.random.randint(0, 2), ctrl_trial])

        return schedule, ['Rewarded', 'Correlated', 'Odour 1 Valve', 'O1 Contributions', 'Odour 2 Valves',
                          'O2 Contributions', 'Blank Valves', 'B Contributions', 'Frequency',
                          'Valence Map', 'Lick Fraction', 'Phase Choice', 'First Odour Choice', 'Control Trial']

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
        phase_choice = trial[11]
        first_odour_choice = trial[12]
        ctrl_trial = trial[13]

        anti_phase_offset = (1.0 / frequency) * 0.5

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
                     'amp_max': 1.0,
                     'extend': False}

            if ctrl_trial > 0.5:

                # is this an odour 1 valve
                if p + 1 in o1_valve:
                    param['length'] = length
                    param['target_duty'] = o1_contr[np.where(o1_valve == p + 1)[0]]
                    if correlated:
                        # param['onset'] += anti_phase_offset * phase_choice
                        if first_odour_choice is 0:
                            param['extend'] = True
                        else:
                            param['onset'] += anti_phase_offset
                    else:
                        # param['onset'] += anti_phase_offset * phase_choice
                        if phase_choice is 1:
                            param['extend'] = True

                # is this an odour 2 valve
                if p + 1 in o2_valve:
                    param['length'] = length
                    param['target_duty'] = o2_contr[np.where(o2_valve == p + 1)[0]]
                    if correlated:
                        # param['onset'] += anti_phase_offset * phase_choice
                        if first_odour_choice is 1:
                            param['extend'] = True
                        else:
                            param['onset'] += anti_phase_offset
                    else:
                        # param['onset'] += anti_phase_offset * (1 - phase_choice)
                        if phase_choice is 0:
                            param['extend'] = True

                # is this a blank valve
                if p + 1 in b_valve:
                    param['length'] = length
                    param['target_duty'] = b_contr[np.where(b_valve == p + 1)[0]]
                    if correlated:
                        if int(np.where(b_valve == p + 1)[0][0]) is 0:
                            param['onset'] += anti_phase_offset * 2.0
                            param['length'] -= anti_phase_offset * 2.0

                    else:
                        if param['target_duty'] != 0.5:
                            param['shadow'] = True
                            param['onset'] += anti_phase_offset
                            param['length'] -= anti_phase_offset
                        else:
                            param['onset'] += anti_phase_offset * np.where(b_valve == p + 1)[0][0]
                            param['onset'] += anti_phase_offset
                            param['length'] -= (anti_phase_offset * (np.where(b_valve == p + 1)[0][0])) * 2.0

            else:

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


class CorrDifficultySwitchWidget(QtWidgets.QWidget, corrDifficultySwitchDesign.Ui_Form):
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

        frequency_low = float(self.pulseLowFrequencyEdit.text())
        frequency_high = float(self.pulseHighFrequencyEdit.text())
        sp_correlated = bool(self.spCorrelatedCheck.isChecked())

        schedule = []
        for t in range(n_trials + n_control_trials):
            # set correlation
            if sp_correlated:
                correlated = True if reward_sequence[t] == 1 else False
            else:
                correlated = False if reward_sequence[t] == 1 else True

            simple_choice = np.random.uniform() > float(self.fractionSimpleTrialsEdit.text())

            if t < n_trials:
                o1_choice = valve_index[1]
                o2_choice = valve_index[2]
                b_choice = valve_index[0]
            else:
                simple_choice = True
                o1_choice = valve_index[3]
                o2_choice = valve_index[2]
                b_choice = np.hstack((valve_index[4], np.random.choice(valve_index[0], 1)))

            if simple_choice:
                # for a simple choice we will always need 1 o1, 1 o2 valves and 2 b valves all at 50% open
                o1_valve = np.random.choice(o1_choice, 1, replace=False) + 1
                o1_contributions = [0.5]

                o2_valve = np.random.choice(o2_choice, 1, replace=False) + 1
                o2_contributions = [0.5]

                b_valve = np.random.choice(b_choice, 2, replace=False) + 1
                b_contributions = [0.5, 0.5]
            # otherwise there are some differences according to correlation structure
            else:
                # can be made up of random combination of 1 or 2 valves, b valve contrs. add to 1
                o1_valve = np.random.choice(o1_choice, np.random.randint(1, len(o1_choice) + 1), replace=False) + 1
                o1_contributions = np.round(np.random.dirichlet(np.ones(len(o1_valve))) * 0.5, 2)

                o2_valve = np.random.choice(o2_choice, np.random.randint(1, 3), replace=False) + 1
                o2_contributions = np.round(np.random.dirichlet(np.ones(len(o2_valve))) * 0.5, 2)

                if correlated:
                    # if correlated we want our blank valves to add to 1 + we always need 2 valves
                    b_valve = np.random.choice(b_choice, 2, replace=False) + 1

                    b_contributions = np.array([1.0, 0.0])
                    while np.prod(b_contributions) == 0:
                        b_contributions = np.round(np.random.dirichlet(np.ones(len(b_valve))), 2)
                else:
                    # else they must add to 0.5
                    b_valve = np.random.choice(b_choice, 2, replace=False) + 1

                    b_contributions = np.array([1.0, 0.0])
                    while np.prod(b_contributions) == 0:
                        b_contributions = np.round(np.random.dirichlet(np.ones(len(b_valve))) * 0.5, 2)

            frequency = np.random.choice([frequency_low, frequency_high], 1)[0]

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


class CorrRandomisedFrequencyWidget(QtWidgets.QWidget, corrRandomFrequencyDesign.Ui_Form):
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

        cycle_min = float(self.cycleLengthLowerEdit.text())
        cycle_max = float(self.cycleLengthUpperEdit.text())
        sp_correlated = bool(self.spCorrelatedCheck.isChecked())

        schedule = []
        for t in range(n_trials + n_control_trials):
            # choose frequency
            cycle_choice = np.random.uniform(cycle_min, cycle_max)
            frequency = int(1000.0 / cycle_choice)

            # set correlation
            if sp_correlated:
                correlated = True if reward_sequence[t] == 1 else False
            else:
                correlated = False if reward_sequence[t] == 1 else True

            simple_choice = np.random.uniform() > float(self.fractionSimpleTrialsEdit.text())

            if t < n_trials:
                o1_choice = valve_index[1]
                o2_choice = valve_index[2]
                b_choice = valve_index[0]
            else:
                simple_choice = True
                o1_choice = valve_index[3]
                o2_choice = valve_index[2]
                b_choice = np.hstack((valve_index[4], np.random.choice(valve_index[0], 1)))

            if simple_choice:
                # for a simple choice we will always need 1 o1, 1 o2 valves and 2 b valves all at 50% open
                o1_valve = np.random.choice(o1_choice, 1, replace=False) + 1
                o1_contributions = [0.5]

                o2_valve = np.random.choice(o2_choice, 1, replace=False) + 1
                o2_contributions = [0.5]

                b_valve = np.random.choice(b_choice, 2, replace=False) + 1
                b_contributions = [0.5, 0.5]
            # otherwise there are some differences according to correlation structure
            else:
                # can be made up of random combination of 1 or 2 valves, b valve contrs. add to 1
                o1_valve = np.random.choice(o1_choice, np.random.randint(1, len(o1_choice) + 1), replace=False) + 1
                o1_contributions = np.round(np.random.dirichlet(np.ones(len(o1_valve))) * 0.5, 2)

                o2_valve = np.random.choice(o2_choice, np.random.randint(1, 3), replace=False) + 1
                o2_contributions = np.round(np.random.dirichlet(np.ones(len(o2_valve))) * 0.5, 2)

                if correlated:
                    # if correlated we want our blank valves to add to 1 + we always need 2 valves
                    b_valve = np.random.choice(b_choice, 2, replace=False) + 1

                    b_contributions = np.array([1.0, 0.0])
                    while np.prod(b_contributions) == 0:
                        b_contributions = np.round(np.random.dirichlet(np.ones(len(b_valve))), 2)
                else:
                    # else they must add to 0.5
                    b_valve = np.random.choice(b_choice, 2, replace=False) + 1

                    b_contributions = np.array([1.0, 0.0])
                    while np.prod(b_contributions) == 0:
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


class CorrRandomisedFrequency2Widget(QtWidgets.QWidget, corrRandomFrequency2Design.Ui_Form):
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

        hz_min = int(self.hzLowerEdit.text())
        hz_max_band_1 = int(self.hzUpperBand1Edit.text())
        hz_max_band_2 = int(self.hzUpperBand2Edit.text())
        hz_max_band_3 = int(self.hzUpperBand3Edit.text())
        sp_correlated = bool(self.spCorrelatedCheck.isChecked())

        schedule = []
        for t in range(n_trials + n_control_trials):
            # choose frequency
            band_choice = np.random.uniform(0, 1)
            if band_choice < 0.75:
                hz_band = range(hz_min, hz_max_band_1)
            elif 0.75 <= band_choice < 0.95:
                hz_band = range(hz_max_band_1, hz_max_band_2)
            else:
                hz_band = range(hz_max_band_2, hz_max_band_3)

            frequency = np.random.choice(hz_band)

            # set correlation
            if sp_correlated:
                correlated = True if reward_sequence[t] == 1 else False
            else:
                correlated = False if reward_sequence[t] == 1 else True

            simple_choice = np.random.uniform() > float(self.fractionSimpleTrialsEdit.text())

            if t < n_trials:
                o1_choice = valve_index[1]
                o2_choice = valve_index[2]
                b_choice = valve_index[0]
            else:
                simple_choice = True
                o1_choice = valve_index[3]
                o2_choice = valve_index[2]
                b_choice = np.hstack((valve_index[4], np.random.choice(valve_index[0], 1)))

            if simple_choice:
                # for a simple choice we will always need 1 o1, 1 o2 valves and 2 b valves all at 50% open
                o1_valve = np.random.choice(o1_choice, 1, replace=False) + 1
                o1_contributions = [0.5]

                o2_valve = np.random.choice(o2_choice, 1, replace=False) + 1
                o2_contributions = [0.5]

                b_valve = np.random.choice(b_choice, 2, replace=False) + 1
                b_contributions = [0.5, 0.5]
            # otherwise there are some differences according to correlation structure
            else:
                # can be made up of random combination of 1 or 2 valves, b valve contrs. add to 1
                o1_valve = np.random.choice(o1_choice, np.random.randint(1, len(o1_choice) + 1), replace=False) + 1
                o1_contributions = np.round(np.random.dirichlet(np.ones(len(o1_valve))) * 0.5, 2)

                o2_valve = np.random.choice(o2_choice, np.random.randint(1, 3), replace=False) + 1
                o2_contributions = np.round(np.random.dirichlet(np.ones(len(o2_valve))) * 0.5, 2)

                if correlated:
                    # if correlated we want our blank valves to add to 1 + we always need 2 valves
                    b_valve = np.random.choice(b_choice, 2, replace=False) + 1

                    b_contributions = np.array([1.0, 0.0])
                    while np.prod(b_contributions) == 0:
                        b_contributions = np.round(np.random.dirichlet(np.ones(len(b_valve))), 2)
                else:
                    # else they must add to 0.5
                    b_valve = np.random.choice(b_choice, 2, replace=False) + 1

                    b_contributions = np.array([1.0, 0.0])
                    while np.prod(b_contributions) == 0:
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


class ShatterValveWidget(QtWidgets.QWidget, shatterValveTestDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

        self.valence_map = None

    def generate_schedule(self, valence_map):
        lick_fraction = float(self.lickFractionEdit.text())
        n_valves = len(valence_map)

        n_trials = int(self.nTrialsEdit.text())

        valence_map = np.array(valence_map)
        valve_index = (np.where(valence_map == 0)[0],
                       np.where(valence_map == 1)[0])

        frequency = float(self.pulseFrequencyEdit.text())

        schedule = []
        for t in range(n_trials):
            o_choice = np.random.choice(valve_index[1], 1) + 1
            b_choice = np.random.choice(valve_index[0], 1) + 1
            amp_target = np.round(np.random.uniform(), 2)

            schedule.append([1, o_choice, b_choice, amp_target, frequency, valence_map, lick_fraction])

        return schedule, ['Rewarded', 'Odour Valve', 'Blank Valve', 'Target Amplitude', 'Frequency', 'Valence Map', 'Lick Fraction']

    def pulse_parameters(self, trial):
        params = list()

        onset = float(self.onsetEdit.text())
        offset = float(self.offsetEdit.text())
        length = float(self.trialLengthEdit.text())
        shatter_hz = float(self.shatterHzEdit.text())
        o_valve = trial[1]
        b_valve = trial[2]
        target_amp = trial[3]
        frequency = trial[4]
        valence_map = trial[5]

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
                     'lick_fraction': trial[6],
                     'shadow': False,
                     'shatter_frequency': shatter_hz,
                     'target_duty': 0.5,
                     'amp_min': 0.0,
                     'amp_max': 1.0}

            # is this an odour 1 valve
            if p + 1 in o_valve:
                param['length'] = length
                param['onset'] += anti_phase_offset * (1 - phase_choice)
                param['target_duty'] = target_amp

            # is this a blank valve
            if p + 1 in b_valve:
                param['length'] = length
                param['onset'] += anti_phase_offset * phase_choice
                param['target_duty'] = target_amp

            params.append(param)

        return params


class CorrDifficultySwitchCameraTriggerWidget(QtWidgets.QWidget, corrDifficultySwitchCameraTriggerDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

        self.valence_map = None

    def generate_schedule(self, valence_map):
        lick_fraction = float(self.lickFractionEdit.text())
        n_valves = len(valence_map)
        cameraFR = float(self.cameraFrEdit.text())

        n_trials = int(self.nTrialsEdit.text())
        n_control_trials = int(self.nControlTrialsEdit.text())
        reward_sequence = Gen.reward_sequence(n_trials + n_control_trials)

        valence_map = np.array(valence_map)
        valve_index = (np.where(valence_map == 0)[0],
                       np.where(valence_map == 1)[0],
                       np.where(valence_map == 2)[0],
                       np.where(valence_map == 3)[0],
                       np.where(valence_map == 4)[0],
                       np.where(valence_map == 5)[0])

        frequency_low = float(self.pulseLowFrequencyEdit.text())
        frequency_high = float(self.pulseHighFrequencyEdit.text())
        sp_correlated = bool(self.spCorrelatedCheck.isChecked())

        schedule = []
        for t in range(n_trials + n_control_trials):
            # set correlation
            if sp_correlated:
                correlated = True if reward_sequence[t] == 1 else False
            else:
                correlated = False if reward_sequence[t] == 1 else True

            simple_choice = np.random.uniform() > float(self.fractionSimpleTrialsEdit.text())
            c_channel = valve_index[5]

            if t < n_trials:
                o1_choice = valve_index[1]
                o2_choice = valve_index[2]
                b_choice = valve_index[0]
            else:
                simple_choice = True
                o1_choice = valve_index[3]
                o2_choice = valve_index[2]
                b_choice = np.hstack((valve_index[4], np.random.choice(valve_index[0], 1)))

            if simple_choice:
                # for a simple choice we will always need 1 o1, 1 o2 valves and 2 b valves all at 50% open
                o1_valve = np.random.choice(o1_choice, 1, replace=False) + 1
                o1_contributions = [0.5]

                o2_valve = np.random.choice(o2_choice, 1, replace=False) + 1
                o2_contributions = [0.5]

                b_valve = np.random.choice(b_choice, 2, replace=False) + 1
                b_contributions = [0.5, 0.5]
            # otherwise there are some differences according to correlation structure
            else:
                # can be made up of random combination of 1 or 2 valves, b valve contrs. add to 1
                o1_valve = np.random.choice(o1_choice, np.random.randint(1, len(o1_choice) + 1), replace=False) + 1
                o1_contributions = np.round(np.random.dirichlet(np.ones(len(o1_valve))) * 0.5, 2)

                o2_valve = np.random.choice(o2_choice, np.random.randint(1, 3), replace=False) + 1
                o2_contributions = np.round(np.random.dirichlet(np.ones(len(o2_valve))) * 0.5, 2)

                if correlated:
                    # if correlated we want our blank valves to add to 1 + we always need 2 valves
                    b_valve = np.random.choice(b_choice, 2, replace=False) + 1

                    b_contributions = np.array([1.0, 0.0])
                    while np.prod(b_contributions) == 0:
                        b_contributions = np.round(np.random.dirichlet(np.ones(len(b_valve))), 2)
                else:
                    # else they must add to 0.5
                    b_valve = np.random.choice(b_choice, 2, replace=False) + 1

                    b_contributions = np.array([1.0, 0.0])
                    while np.prod(b_contributions) == 0:
                        b_contributions = np.round(np.random.dirichlet(np.ones(len(b_valve))) * 0.5, 2)

            frequency = np.random.choice([frequency_low, frequency_high], 1)[0]

            schedule.append([reward_sequence[t], correlated, o1_valve, o1_contributions, o2_valve, o2_contributions,
                             b_valve, b_contributions, frequency, valence_map, lick_fraction, c_channel + 1, cameraFR])

        return schedule, ['Rewarded', 'Correlated', 'Odour 1 Valve', 'O1 Contributions', 'Odour 2 Valves',
                          'O2 Contributions', 'Blank Valves', 'B Contributions', 'Frequency',
                          'Valence Map', 'Lick Fraction', 'Camera Channel', 'Camera Frame Rate']

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
        c_channel = trial[11]
        frame_rate = trial[12]

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

            # is this a camera channel?
            if p + 1 in c_channel:
                param['length'] = length + onset + 1.0
                param['type'] = 'Simple'
                param['frequency'] = frame_rate
                param['onset'] = 0.0

            params.append(param)

        return params
