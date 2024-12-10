import pickle
from nltk.tag import tnt 
from preprocess import load_conllu

if __name__ == "__main__":
    train_data = load_conllu("data/cs_cac-ud-train.conllu")
    tnt_tagger = tnt.TnT()
    tnt_tagger.train(train_data)

    with open("tnt_tagger.pickle", "wb") as file:
        pickle.dump(tnt_tagger, file)