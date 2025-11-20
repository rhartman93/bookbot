import sys

from stats import char_counts, char_count_list, word_count

def get_book_text(local_file: str):
    with open(local_file) as book_file:
        book_text = book_file.read()
    return book_text


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_text = get_book_text(book)
    count = word_count(book_text)
    char_map = char_counts(book_text)
    report_list = char_count_list(char_map)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for character in report_list:
        print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")
main()