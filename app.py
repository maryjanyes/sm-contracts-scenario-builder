# Smart Contracts Scenario builder
# SmartContractsBuilder - app entry point

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import Qt

# from src.speech_recognizer import SmartContractsBuilder_SpeechRecognizer
from src.speech_recorder import SmartContractsBuilder_SpeechRecorder
from src.constants import app_scenarios_dir
from src.ui_app_styles import *
from src.user.model import UserCryptoSettings
from builder.builder import SmartContractsBuilder_Builder

# def deploy_test_scenario():
#    test_contract_header = "// SPDX-License-Identifier: GPL-3.0pragma solidity >=0.4.0 <0.9.0;"
#    test_contract_body = "contract C { struct S { uint16 a; uint16 b; uint256 c; } uint x; mapping(uint => mapping(uint => S)) data; }"

#    app.deploy_scenario(test_contract_header + test_contract_body, 'MyScenario')

builder = SmartContractsBuilder_Builder()
block_scenarios = builder.interactive_block_scenarios_data()


class SmartContractsBuilder():
    def __init__(self):
        # _self.speech_recognizer = SmartContractsBuilder_SpeechRecognizer()
        self.speech_recorder = SmartContractsBuilder_SpeechRecorder()

    def create_new_voice_scenario(self):
        file_name = ''
        self.speech_recorder.start_recording(file_name)

    def deploy_scenario(self):
        contract_script = self.parent.scenario_content_label.text() + '\n}'
        contract_name = 'MyContract'
        scenario_solidity_file = open(
            app_scenarios_dir + contract_name + '.sol', 'a')
        scenario_solidity_file.write(contract_script)
        # TODO: Run deploy script on created contract

    def build_profile():
        user_settings = UserCryptoSettings()
        print(user_settings.wallet_address)


class UIApp(QWidget):
    def __init__(self, builder):
        super().__init__()

        self.builder = builder
        self.setWindowTitle('Smart Contracts Scenarios builder')
        layout = QGridLayout()
        self.setFixedHeight(800)
        self.setFixedWidth(1200)
        self.setLayout(layout)
        layout.setAlignment(Qt.AlignLeft)
        self.show_scenarios(layout=layout)
        self.builder.parent = self
        create_scenario_button = QPushButton('Create Scenario')
        create_scenario_button.clicked.connect(self.builder.deploy_scenario)
        layout.addWidget(create_scenario_button)
        helper_label = QLabel(self)
        helper_label.setText('Solidity Contract script: ' + '\n')
        helper_label.setStyleSheet(help_content_box_style)
        helper_label.setFixedWidth(self.width())
        helper_label.setFixedHeight(100)
        helper_label.move(450, 100)
        scenario_label = QLabel(self)
        scenario_label.setText(
            '// SPDX-License-Identifier: MIT;\ncontract MyContract {\nconstructor() public { }\n')
        scenario_label.move(450, 0)
        scenario_label.setFixedWidth(self.width())
        scenario_label.setFixedHeight(self.height())
        scenario_label.setStyleSheet(scenario_content_box_style)
        self.scenario_content_label = scenario_label
        self.show()

    def show_scenarios(self, layout):
        count = 0
        for scenario in block_scenarios['BlockName']:
            scenario_button = QPushButton(str(count + 1) + ': ' + scenario)
            scenario_button.clicked.connect(self.select_scenario)
            scenario_button.setFixedWidth(350)
            layout.addWidget(scenario_button, count, 0)
            count = count + 1

    def select_scenario(self):
        sender = self.sender().text()
        scenario_index = sender.split(':')[0]
        scenario_script = block_scenarios['BlockScript'][int(
            scenario_index) - 1]
        scenario_content = self.scenario_content_label.text() + '\n' + scenario_script
        self.scenario_content_label.setText(scenario_content)


app = QApplication([])
ui_app = UIApp(SmartContractsBuilder())
app.exec()
