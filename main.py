import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "books", "frankenstein.txt")

def main():
    contents = read_file(file_path)
    # print(contents)
    print(f"--- Begin report of {file_path} ---")
    print(f"{count_words(contents)} words found in the document.")
    letters = count_characters(contents)
    for letter in letters:
        print(f"The {letter} character was found {letters[letter]} times")

    
def read_file(file_name):
    with open(file_name) as f:
        file_contents = f.read()
        return file_contents
    
def count_words(book_text):
    words = book_text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(book_text):
    # Convert text to lowercase
    book_text = book_text.lower()
    
    # Initialize the dictionary for a-z with 0 counts
    letters = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
        "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
        "y": 0, "z": 0
    }
    
    # Iterate over each character in the text
    for char in book_text:
        match char:
            case _ if char in letters:  # Check if it's an alphabetic character (a-z)
                letters[char] += 1
            case _:  # For any other characters
                if char in letters:
                    letters[char] += 1  # Increment count if it's already been encountered
                else:
                    letters[char] = 1   # Add the new character to the dictionary

    return letters

main()