import sys
import inspect

from PyQt5 import QtWidgets
from Designs import mainDesign
from Models import Widgets

from Models import ScheduleWidgets, ScheduleView


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

        # add function bindings
        self.generateScheduleButton.clicked.connect(self.generate)

        self.scheduleTypesCombo.activated.connect(self.select_schedule_type)

    def generate(self):
        # get the schedule data and headers
        self.schedule, self.schedule_headers = self.current_schedule_type.generate_schedule(self.valence_map.get_valence_map())

        # post to the schedule view
        self.schedule_model = ScheduleView.ScheduleModel(self.schedule_headers, self.schedule, parent=self)
        self.scheduleView.setModel(self.schedule_model)

    def select_schedule_type(self):
        schedule_name = self.scheduleTypesCombo.currentText()

        if self.current_schedule_type is not None:
            self.scheduleParamsContents.layout().removeWidget(self.current_schedule_type)

        self.current_schedule_type = self.schedule_types[schedule_name]()
        self.scheduleParamsContents.layout().addWidget(self.current_schedule_type)


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