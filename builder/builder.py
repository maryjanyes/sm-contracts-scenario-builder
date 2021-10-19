# Smart Contracts Scenario builder
# SmartContractsBuilder_builder - Builder model
# building contract scenario base on received text from user

from builder.csv_files_importer import import_touchable_data


class SmartContractsBuilder_Builder():
    def __init__(_self):
        print("__init__")

    def interactive_block_scenarios_data(_self):
        touchable_scenarios = import_touchable_data()
        return touchable_scenarios
