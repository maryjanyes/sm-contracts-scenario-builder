import csv

scenariosFolder = './solidity-scenarios-data/'


def import_touchable_data():
    scenarios = dict()

    with open(scenariosFolder + 'touchable_data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        index = 0
        first_row = None

        for row in csvreader:
            if index == 0:
                first_row = row
                for scenario_header in row:
                    scenarios[scenario_header] = []
            else:
                index_row = 0
                for scenario_row in row:
                    scenarios[first_row[index_row]].append(scenario_row)
                    index_row = index_row + 1

            index = index + 1

        return scenarios


def import_voice_data():
    return open(scenariosFolder + 'voice_data.csv')


def import_default_data():
    return open(scenariosFolder + 'contract-standard-instructions.csv')
