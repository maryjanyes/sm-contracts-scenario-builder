# Smart Contracts Scenario builder
# SmartContractsBuilder - app entry point

from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QMainWindow, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel

from src.speech_recognizer import SmartContractsBuilder_SpeechRecognizer
from src.speech_recorder import SmartContractsBuilder_SpeechRecorder
from src.constants import app_scenarios_dir
from builder.builder import SmartContractsBuilder_Builder

import sys

# def deploy_test_scenario():
#    test_contract_header = "// SPDX-License-Identifier: GPL-3.0pragma solidity >=0.4.0 <0.9.0;"
#    test_contract_body = "contract C { struct S { uint16 a; uint16 b; uint256 c; } uint x; mapping(uint => mapping(uint => S)) data; }"

#    app.deploy_scenario(test_contract_header + test_contract_body, 'MyScenario')

builder = SmartContractsBuilder_Builder()
block_scenarios = builder.interactive_block_scenarios_data()


class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)
        self.get_start_view_button = QPushButton('Get menu page')
        self.get_start_view_button.move(50, 350)


class TouchableScenariosWidget(QWidget):
    def __init__(self, parent=None):
        super(TouchableScenariosWidget, self).__init__(parent)
        self.create_scenario_button = QPushButton('Create Scenario')
        self.create_scenario_button.move(100, 350)

    def create_scenario():
        print("..")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(600, 400, 600, 400)
        self.show_program_menu()

    def show_program_menu(self):
        self.scenarios_widget = TouchableScenariosWidget(self)
        self.setWindowTitle("Smart Scenario Builder")
        layout = QGridLayout()
        layout.addWidget(self.window.get_start_view_button)
        self.setCentralWidget(self.scenarios_widget)
        self.scenarios_widget.create_scenario_button.clicked.connect(
            self.show_scenarios_widget)
        self.show()

    def show_scenarios_widget(self):
        self.window = UIWindow(self)
        layout = QGridLayout()
        for scenario in block_scenarios:
            scenario_button = QPushButton(scenario)
            scenario_button.setStyleSheet(
                "QLineEdit { background-color: #ffffff }")
            layout.addWidget(scenario_button)
        self.window.setLayout(layout)
        self.setWindowTitle("Build your SmartContract")
        self.setCentralWidget(self.window)
        self.window.get_start_view_button.clicked.connect(
            self.show_program_menu)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_window = MainWindow()
    sys.exit(app.exec_())


class SmartContractsBuilder():
    def __init__(self):
        # _self.speech_recognizer = SmartContractsBuilder_SpeechRecognizer()
        self.speech_recorder = SmartContractsBuilder_SpeechRecorder()

    def connect_profile(self):
        print("Get profile..")

    def create_new_voice_scenario(self):
        file_name = './test-speech-data/my_record_2.wav'
        self.speech_recorder.start_recording(file_name)

    def deploy_scenario(self, contract_content, contract_name):
        scenario_solidity_file = open(
            app_scenarios_dir + contract_name + '.sol', 'a')
        scenario_solidity_file.write(contract_content)
        # TODO: run deploy script for scenario


app = SmartContractsBuilder()
