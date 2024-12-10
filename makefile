DATA_URL = https://github.com/UniversalDependencies/UD_Czech-CAC/archive/refs/tags/r2.15.tar.gz
DATA_ARCHIVE = ud_czech_cac.tar.gz
DATA_DIR = data
TNT_TAGGER = tnt_tagger.pickle

all: readme download train eval show

readme:
	@echo "I used NLTK as it seemed easirier for the first experoencd and it turned out exactly it. For training i used tnt. As a dataset I first used CLTT Treebank (36K) which gave the accuracy around 76%. But for my example sentences it showed most of the words as unknown. Then I tired training the model on CAC (495K), which went much better with accuracy around 86% and did decent for my sample sentences. "

download:
	wget -O $(DATA_ARCHIVE) $(DATA_URL)
	tar -xzf $(DATA_ARCHIVE)
	mkdir -p $(DATA_DIR)
	mv cs_cac-ud-*.conllu $(DATA_DIR)
	rm -rf UD_Czech-CAC-2.15
	rm -f $(DATA_ARCHIVE)


train: $(DATA_DIR)/cs_cac-ud-train.conllu 
	python preprocess.py
	python train.py

eval: $(TNT_TAGGER) $(DATA_DIR)/cs_cac-ud-test.conllu 
	python evaluate.py

show: $(TNT_TAGGER)
	python show.py

clean:
	rm -f $(TNT_TAGGER)



