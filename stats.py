def num(n):
    return n["num"]

def get_book_text(file):
    with open(file) as f:
        file_content = f.read()
        return file_content
    

def number_of_words(words):
    num_words = words.split()
    return len(num_words)

def number_of_chars(text):
    character = {}
    for t in text:
        low = t.lower()
        if low in character:
            character[low] += 1
        else:
            character[low] = 1
    return character

def sort_chars(chars):
    sort_char = {}
    test = []
    for c in chars:
        sort_char["char"] = c
        sort_char["num"] = chars[c]
        test.append(sort_char)
        sort_char = {}
    test.sort(reverse=True, key=num)
    return test

