from stats import get_num_words
from stats import get_character_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_list = get_character_count(text)
    print(f"{num_words} words found in the document")
    print(characters_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()