import csv
from Observation import Observation
def read_observations_from_file( observations_filename):
    observations = []
    with open(observations_filename, newline='') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            observations.append(Observation(line[0:-1], line[-1]))
    return observations
def read_test_observations_from_file( observations_filename):
    observations = []
    with open(observations_filename, newline='') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            observations.append(Observation(line[0:], 'test'))
    return observations