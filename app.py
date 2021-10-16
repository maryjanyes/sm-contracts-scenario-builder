# Smart Contracts Scenario builder
# SmartContractsBuilder - app entry point

from src.speech_recognizer import SmartContractsBuilder_SpeechRecognizer
from src.speech_recorder import SmartContractsBuilder_SpeechRecorder

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget

import sys
from src.constants import app_scenarios_dir

# def deploy_test_scenario():
#    test_contract_header = "// SPDX-License-Identifier: GPL-3.0pragma solidity >=0.4.0 <0.9.0;"
#    test_contract_body = "contract C { struct S { uint16 a; uint16 b; uint256 c; } uint x; mapping(uint => mapping(uint => S)) data; }"

#    app.deploy_scenario(test_contract_header + test_contract_body, 'MyScenario')

class SmartContractsBuilder():
    def __init__(_self):
        _self.speech_recognizer = SmartContractsBuilder_SpeechRecognizer()
        _self.speech_recorder = SmartContractsBuilder_SpeechRecorder()
        _self.create_app_ui()

    def create_app_ui(_self):
        app = QApplication(sys.argv)
        start_scenario_widget = _self.create_start_scenario_widget()
        start_scenario_widget.show()
        sys.exit(app.exec_())

    def create_start_scenario_widget(_self):
        window = QWidget()
        layout = QHBoxLayout()

        window.setWindowTitle('Smart Scenario Builder')
        window.setGeometry(600, 400, 600, 400)
        recordButton = QPushButton('Record Scenario')
        connectProfileButton = QPushButton('Connect Profile')

        recordButton.clicked.connect(_self.create_new_scenario)
        connectProfileButton.clicked.connect(_self.connect_profile)
        layout.addWidget(recordButton)
        layout.addWidget(connectProfileButton)
        window.setLayout(layout)

        return window

    def connect_profile(_self):
        _self.create_profile_widget()

    def create_profile_widget(_self):
        print("Soon..")

    def create_new_scenario(_self):
        file_name = './test-speech-data/my_record_2.wav'
        _self.speech_recorder.start_recording(file_name)

    def deploy_scenario(_self, contract_content, contract_name):
        scenario_solidity_file = open(
            app_scenarios_dir + contract_name + '.sol', 'a')
        scenario_solidity_file.write(contract_content)
        # TODO: run deploy script for scenario


app = SmartContractsBuilder()
