from stats import get_num_words
from stats import get_character_count
from stats import dict_sorter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_list = get_character_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f" Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = dict_sorter(characters_list)
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()