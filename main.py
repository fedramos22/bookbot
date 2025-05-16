import sys
from stats import (
    count_words, 
    count_characters, 
    get_book_text,
    chars_dict_to_sorted_list,
    )

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    book_path= sys.argv[1]

    book = get_book_text(book_path)
    count_text = count_words(book)
    chars_dict = count_characters(book)
    chars_sorted_list= chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, count_text, chars_sorted_list)

def print_report(book_path, count_text, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_text} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()