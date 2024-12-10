def load_conllu(filepath):
    sentences = []

    with open(filepath, encoding="utf-8") as file:
        sentence = []
        for line in file:
            if line.startswith('#') or not line.strip():
                if (sentence):
                    sentences.append(sentence)
                    sentence = []
                continue
            
            line_parts = line.split('\t')
            if len(line_parts) > 3:
                word, pos = line_parts[1], line_parts[3]
                sentence.append((word, pos))
    
    return sentences

