def main():
    book = "books/frankenstein.txt"
    text = get_book(book)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document\n")

    for key in sorted_char_count.keys():
        print(f"The '{key}' character was found {sorted_char_count[key]} times")

    print("--- End report ---")


def sort_on(dict):
    return dict["num"]


def get_book(path):
    with open(path) as book:
        contents = book.read()
        return contents


def count_words(str):
    words = str.split()
    return len(words)


def count_chars(str):
    result = {}

    for _char in str:
        char = _char.lower()
        try:
            result[char] = result[char] + 1
        except KeyError:
            result[char] = 1

    return result


main()