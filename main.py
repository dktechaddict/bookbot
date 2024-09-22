import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "books", "frankenstein.txt")

def main():
    contents = read_file(file_path)
    print(contents)
    print(f"There are {count_words(contents)} words in the book.")
    
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

main()