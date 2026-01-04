from stats import get_num_words, get_chars_count, get_sorted_list
import sys

book_path = "books/frankenstein.txt"

def get_book_text(book_path):
    with open(book_path) as f:
        book_content = f.read()
    return book_content

def print_book_report(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")    
    book_text = get_book_text(book_path)
    num_words: int = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_counts = get_chars_count(book_text)
    print("--------- Character Count -------")
    for stat in get_sorted_list(char_counts):
        if stat['char'].isalpha():
            print(f"  {stat['char']}: {stat['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print_book_report(book_path)

if __name__ == "__main__":
    main()