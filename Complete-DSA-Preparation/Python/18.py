import string

def remove_punctuation(s):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)
    
    # Use the translate method to remove punctuation
    return s.translate(translator)

# Example usage
input_string = "Let's try, Mike."
cleaned_string = remove_punctuation(input_string)
print(f"Original: {input_string}")
print(f"Without punctuation: {cleaned_string}")
