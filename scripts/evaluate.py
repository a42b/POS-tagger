import pickle
from nltk.tag import tnt 
from preprocess import load_conllu

if __name__ == "__main__":
    test_data = load_conllu("data/cs_cac-ud-test.conllu")
    with open("tnt_tagger.pickle", "rb") as file:
        tnt_tagger = pickle.load(file)
        accuracy = tnt_tagger.accuracy(test_data)

    print(f"Accuracy: {accuracy}")