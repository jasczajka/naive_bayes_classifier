from Observation import Observation
from util import read_observations_from_file
class Classifier:
    def __init__(self, observations_filename):
        self.observations = read_observations_from_file(observations_filename)
        self.possible_values = {}
        self.possible_outcomes = {}
        #for each attribute
        for i in range(len(self.observations[0].attributes)):
            #first a list of possibilitites
            self.possible_values[i] = []
            for observation in self.observations:
                self.possible_values[i].append(observation.attributes[i])
        #convert the lists to sets so we have unique possibilities for each attribute
        for possible_value in self.possible_values.items():
            self.possible_values[possible_value[0]] = set(possible_value[1])
        print(self.possible_values)

        possible_outcomes_list = []
        for observation in self.observations:
            possible_outcomes_list.append(observation.actual_classification)
        self.possible_outcomes = set(possible_outcomes_list)
        print(self.possible_outcomes)


    def classify(self, observation_to_classify):
        probabilities = {}
        for possible_outcome in self.possible_outcomes:
            #first lets get p(y)
            observations_y = [observation for observation in self.observations if observation.actual_classification == possible_outcome]
            probability = len(observations_y)/len(self.observations)
            print('p(y): ', probability)
            #then for each attribute
            for i in range (len(observation_to_classify.attributes)):
                #count only from those that have same outcome and same attribute that we are currently checking
                observations_attribute = [observation for observation in observations_y if observation_to_classify.attributes[i] == observation.attributes[i]]
                #laplace
                if(len(observations_attribute) == 0):
                    count = 1
                    count_attribute =  len(self.possible_values[i])
                    probability *= count/count_attribute
                    print("using laplace, propability for ", observation_to_classify.attributes[i], ' with ',possible_outcome, ' is ',count/count_attribute)
                else:
                    count = len(observations_attribute)
                    probability *= count/len(observations_y)
                    print("propability for ", observation_to_classify.attributes[i], ' with', possible_outcome, ' is ',count/len(observations_y))


            probabilities[possible_outcome] = probability

        print(probabilities)
        return sorted(probabilities, key = lambda x:x[1], reverse=True)[0]
