import sys
import inspect
import numpy as np
import pickle

from PyQt5 import QtWidgets
from Designs import mainDesign
from Models import Widgets

from Models import ScheduleWidgets, ScheduleView
from UI import ColorMap
from PyPulse import PulseInterface


class MainApp(QtWidgets.QMainWindow, mainDesign.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.current_schedule_type = None
        self.schedule = dict()
        self.schedule_headers = []

        # add the reward map
        self.valence_map = Widgets.ValveMapWidget(self.valveMapContents)
        self.valveMapContents.layout().addWidget(self.valence_map)

        # populate schedule types
        self.schedule_types = dict()
        for name, obj in inspect.getmembers(ScheduleWidgets):
            if inspect.isclass(obj):
                self.scheduleTypesCombo.addItem(name)
                self.schedule_types[name] = obj

        # initialise schedule model
        self.scheduleView.setModel(ScheduleView.ScheduleModel([], [[]]))

        # add function bindings
        self.actionSave.triggered.connect(self.save_schedule)

        self.generateScheduleButton.clicked.connect(self.generate)

        self.scheduleTypesCombo.activated.connect(self.select_schedule_type)

        self.scheduleView.selectionModel().selectionChanged.connect(self.draw_pulse)

    def generate(self):
        # get the schedule data and headers
        self.schedule, self.schedule_headers = self.current_schedule_type.generate_schedule(self.valence_map.get_valence_map())

        # post to the schedule view
        self.schedule_model = ScheduleView.ScheduleModel(self.schedule_headers, self.schedule, parent=self)
        self.scheduleView.setModel(self.schedule_model)
        self.scheduleView.selectionModel().selectionChanged.connect(self.draw_pulse)

    def select_schedule_type(self):
        schedule_name = self.scheduleTypesCombo.currentText()

        if self.current_schedule_type is not None:
            self.scheduleParamsContents.layout().removeWidget(self.current_schedule_type)
            self.current_schedule_type.deleteLater()

        self.current_schedule_type = self.schedule_types[schedule_name]()
        self.scheduleParamsContents.layout().addWidget(self.current_schedule_type)

        self.scheduleView.setModel(ScheduleView.ScheduleModel([], [[]]))

    def draw_pulse(self):
        trial = self.schedule[self.scheduleView.selectionModel().selectedRows()[0].row()]
        params = self.current_schedule_type.pulse_parameters(trial)
        for p in params:
            print(p['target_duty'])
        print('--------------------')

        pulses, t = PulseInterface.make_pulse(20000.0, 0.0, 0.0, params)

        self.pulseView.plotItem.clear()
        for p, pulse in enumerate(pulses):
            color = ColorMap.c_list[self.valence_map.get_valence_map()[p]]
            self.pulseView.plotItem.plot(t, np.array(pulse) - (p*1.1), pen=color)

    def save_schedule(self):
        params = list()
        for trial in self.schedule:
            params.append(self.current_schedule_type.pulse_parameters(trial))

        fname, suff = QtWidgets.QFileDialog.getSaveFileName(self, "Save Schedule", '', "Schedule File (*.schedule)")
        try:
            with open(fname, 'wb') as fn:
                pickle.dump({'schedule': self.schedule,
                             'headers': self.schedule_headers,
                             'params': params}, fn)
        except:
            pass


# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainApp()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()