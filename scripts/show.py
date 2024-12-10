import pickle
from nltk.tag import tnt 
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == "__main__":
    with open("tnt_tagger.pickle", "rb") as file:
        tnt_tagger = pickle.load(file)
    
    sample_sentences = [
        "Dal bych si jedno pivo.",
        "Toto je ukázková věta.",
        "Programujeme v Pythonu."
    ]

    for sentence in sample_sentences:
        words = sentence.split()
        tagged_sentence = tnt_tagger.tag(words) 

        print(f"Sentence: {sentence}")
        for word, pos in tagged_sentence:
            print(f"{word}: {pos}")
