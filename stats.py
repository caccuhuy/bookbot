def get_book_text(path):
    with open(path) as f:
        return f.read().lower()
def count_word(path):
    a=list(get_book_text(path).lower().split())
    return len(a)
def count_char(path):
    dictionary = {}
    for char in get_book_text(path):
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary