from PyQt5 import QtWidgets
import numpy as np

from Designs import basicGNGDesign, v8CorrDesign, simpleCorrDesign
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


class SimpleCorrWidget(QtWidgets.QWidget, simpleCorrDesign.Ui_Form):
    def __init__(self, parentUi=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.parentUi = parentUi

        self.valence_map = None

    def generate_schedule(self, valence_map):
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

            schedule.append([reward_sequence[t], correlated, o1_valve, o2_valve, b_valves, frequency, valence_map])

        return schedule, ['Rewarded', 'Correlated', 'Odour 1 Valve', 'Odour 2 Valves', 'Blank Valves', 'Frequency',
                          'Valence Map']

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
                     'chop_amount': 0.25}

            # is this an odour 1 valve
            if p + 1 in o1_valve:
                param['length'] = length
                if correlated:
                    param['offset'] += anti_phase_offset

            # is this an odour 2 valve
            if p + 1 in o2_valve:
                param['length'] = length
                if not correlated:
                    param['onset'] += anti_phase_offset

            # is this a blank valve
            if p + 1 in b_valves:
                param['length'] = length
                if correlated:
                    param['onset'] += anti_phase_offset
                else:
                    param['onset'] += anti_phase_offset * np.where(b_valves == p + 1)[0][0]

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

        # generate reward sequence
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
        frequency = float(self.pulseFrequencyEdit.text())
        amp_min = float(self.shatterDutyMinEdit.text())
        amp_max = float(self.shatterDutyMaxEdit.text())
        nControlTrials = int(self.nControlTrialsEdit.text())
        single_valve_trials = float(self.fractionSingleValveEdit.text())
        sp_correlated = bool(self.spCorrelatedCheck.isChecked())

        shatter_bounds = (amp_max - amp_min)

        # algorithm for generating trials
        schedule = []
        for t in range(n_trials):
            # set correlation
            if sp_correlated:
                correlated = True if reward_sequence[t] == 1 else False
            else:
                correlated = False if reward_sequence[t] == 1 else True

            # 1. how many valves will odour 1 use + relative contribution
            v_decision = np.random.uniform() <= single_valve_trials
            o1_v = np.random.choice(valve_index[1], 1) + 1 if v_decision else np.random.choice(valve_index[1], 2, replace=False) + 1
            if len(o1_v) > 1:
                o1_contribution = ((np.random.dirichlet(np.ones(len(o1_v))) * shatter_bounds) + amp_min) / 2.0
            else:
                o1_contribution = [0.5]
            o1_contribution = np.round(o1_contribution, 2)

            # 2. how many valves will odour 2 use + relative contribution
            v_decision = np.random.uniform() <= single_valve_trials
            o2_v = np.random.choice(valve_index[2], 1) + 1 if v_decision else np.random.choice(valve_index[2], 2, replace=False) + 1
            if len(o2_v) > 1:
                o2_contribution = ((np.random.dirichlet(np.ones(len(o2_v))) * shatter_bounds) + amp_min) / 2.0
            else:
                o2_contribution = [0.5]
            o2_contribution = np.round(o2_contribution, 2)

            # blank valve contributions
            v_decision = np.random.uniform() <= single_valve_trials
            if correlated:
                b_v = np.random.choice(valve_index[0], 2, replace=False) + 1
                b_contribution = ((np.random.dirichlet(np.ones(len(b_v))) * shatter_bounds) + amp_min) if v_decision else [0.5, 0.5]
            else:
                b_v = np.random.choice(valve_index[0], 2, replace=False) + 1
                b_contribution = ((np.random.dirichlet(np.ones(2)) * shatter_bounds) + amp_min) / 2.0 if v_decision else [0.5, 0.5]
            b_contribution = np.round(b_contribution, 2)

            if correlated:
                # place position 1 valves and contributions
                p1_valves = np.hstack((o1_v, o2_v))
                p1_contribution = np.hstack((o1_contribution, o2_contribution))

                # place position 2 valves and contributions
                p2_valves = b_v
                p2_contribution = b_contribution
            else:
                # place valves and contributions
                if b_contribution[0] == 0.5:
                    p1_valves = np.hstack((o1_v, b_v[0]))
                    p1_contribution = np.hstack((o1_contribution, b_contribution[0]))

                    p2_valves = np.hstack((o2_v, b_v[1]))
                    p2_contribution = np.hstack((o2_contribution, b_contribution[1]))
                else:
                    p1_valves = np.hstack((o1_v, b_v[0], b_v[1]))
                    p1_contribution = np.hstack((o1_contribution, b_contribution[0], b_contribution[1]))

                    p2_valves = np.hstack((o2_v, b_v[0], b_v[1]))
                    p2_contribution = np.hstack((o2_contribution, b_contribution[1], b_contribution[0]))

            schedule.append([reward_sequence[t], correlated, p1_valves, p1_contribution, p2_valves, p2_contribution,
                             frequency, valence_map])

        return schedule, ['Rewarded', 'Correlated', 'Position 1 Valves', 'Position 1 Contribtions', 'Position 2 Valves',
                          'Position 2 Contributions', 'Frequency', 'Valence Map']

    def pulse_parameters(self, trial):
        valence_map = trial[7]
        params = list()

        onset = float(self.onsetEdit.text())
        offset = float(self.offsetEdit.text())
        length = float(self.trialLengthEdit.text())
        shatter_frequency = float(self.shatterFrequencyEdit.text())
        amp_min = float(self.shatterDutyMinEdit.text())
        amp_max = float(self.shatterDutyMaxEdit.text())

        anti_phase_offset = (1.0 / trial[6]) * 0.5

        # compiled_valves = [item for sublist in [trial[2], trial[4], trial[6]] for item in sublist]
        # compiled_contributions = [np.round(item, 2) for sublist in [trial[3], trial[5], trial[7]] for item in sublist]

        for p in range(len(valence_map)):
            param = {'type': 'RandomNoise',
                     'fromDuty': True,
                     'fromValues': False,
                     'frequency': trial[6],
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
                     'amp_max': amp_max,
                     'shadow': False}

            params.append(param)

            # are we in a correlated trial?
            if trial[1]:
                # is this an active odour 1 valve?
                if p in np.where(valence_map == 1)[0] and (p + 1) in trial[2]:
                    # then we set this valve for odour 1 to active
                    param['length'] = length
                    param['target_duty'] = trial[3][np.where(trial[2] == p + 1)[0]]
                # is this an active odour 2 valve?
                elif p in np.where(valence_map == 2)[0] and (p + 1) in trial[2]:
                    # then we set this valve for odour 2 to active
                    param['length'] = length
                    param['target_duty'] = trial[3][np.where(trial[2] == p + 1)[0]]
                # is this an active blank valve?
                elif p in np.where(valence_map == 0)[0] and (p + 1) in trial[4]:
                    # then we set this valve for blank to active
                    param['length'] = length
                    param['target_duty'] = trial[5][np.where(trial[4] == p + 1)[0]]
                    param['onset'] += anti_phase_offset
            # else we are in an anti-correlated trial
            else:
                # is this an active odour 1 valve?
                if p in np.where(valence_map == 1)[0] and (p + 1) in trial[2]:
                    # then we set this valve for odour 1 to active
                    param['length'] = length
                    param['target_duty'] = trial[3][np.where(trial[2] == p + 1)[0]]
                # is this an active odour 2 valve
                elif p in np.where(valence_map == 2)[0] and (p + 1) in trial[4]:
                    # then we set this valve for odour 2 to active and put it in antiphase
                    param['length'] = length
                    param['target_duty'] = trial[5][np.where(trial[4] == p + 1)[0]]
                    param['onset'] += anti_phase_offset
                # is this an active blank valve in position 1?
                elif p in np.where(valence_map == 0)[0] and (p + 1) in trial[4]:
                    param['length'] = length
                    param['target_duty'] = trial[3][np.where(trial[2] == p + 1)[0]]
                    param['shadow'] = True

        return params
