import random

def create_sentence_with_typos(sentence, count, num_typos):
    words = sentence.split()
    sentences = []
    
    for i in range(count):
        sentence_with_typos = []
        for word in words:
            if random.random() < num_typos / count:
                typo_index = random.randint(0, len(word) - 1)
                typo_word = word[:typo_index] + random.choice('abcdefghijklmnopqrstuvwxyz') + word[typo_index + 1:]
                sentence_with_typos.append(typo_word)
            else:
                sentence_with_typos.append(word)
        
        sentences.append(f"{i + 1}. {' '.join(sentence_with_typos)}")
    
    return sentences

def main():
    sentence = "I will never spam my friends again."
    count = 100
    num_typos = 8
    
    sentences = create_sentence_with_typos(sentence, count, num_typos)
    
    for s in sentences:
        print(s)

if __name__ == "__main__":
    main()
