from stats import number_of_words, get_book_text, number_of_chars, sort_chars

def main():
    book_path = "/home/ubuntu/workspace/github/bookbot/books/frankenstein.txt"
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
main()