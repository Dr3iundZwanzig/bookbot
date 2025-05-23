from stats import number_of_words, get_book_text, number_of_chars, sort_chars
import sys

def main():
    from sys import argv
    main, path = argv

    book_path = path
    book = get_book_text(book_path)
    num_words = number_of_words(book)
    chars = number_of_chars(book)
    chars_sorted = sort_chars(chars)





    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for w in chars_sorted:
        if not w["char"].isalpha():
            continue
        print(f"{w['char']}: {w['num']}")
    print("============= END ===============")

try:
      main()  
except ValueError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
