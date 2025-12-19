import sys
from stats import get_word_count, get_char_counts, sort_char_dict

def get_book_text(path: str):
    
    with open(path) as f:
        book_blob = f.read()
    
    return book_blob

def print_display(path: str, wc: int, char_list: list):
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")

    for item in char_list:
        print(f"{item["char"]}: {item["num"]}")

def main():

    if len(sys.argv) < 2:
        
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_blob = get_book_text(path)
    word_count = get_word_count(book_blob)
    sorted_char_list = (sort_char_dict(get_char_counts(book_blob)))

    print_display(path, word_count, sorted_char_list)

if __name__ == "__main__":
    main()