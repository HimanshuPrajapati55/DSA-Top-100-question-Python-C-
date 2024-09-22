def count_word_frequencies(text):
    words = text.split()
    frequencies = {}
    
    for word in words:
        word = word.lower()
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    
    return frequencies

def main():
    text = input("Enter a list of words separated by whitespace: ")
    frequencies = count_word_frequencies(text)
    
    print("Word frequencies:")
    for word, count in frequencies.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
