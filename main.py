from Classifier import Classifier
from util import read_observations_from_file
from util import read_test_observations_from_file
def main():
    classifier = Classifier("trainingset.csv")
    test_observations = read_test_observations_from_file("testset.csv")
    for test_observation in test_observations:
        print(classifier.classify(test_observation))
if __name__ == "__main__":
    main()


