from stats import get_word_count, get_char_counts, sort_char_dict

def get_book_text():
    
    with open('./books/frankenstein.txt') as f:
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

    word_count = get_word_count(get_book_text())
    sorted_char_list = (sort_char_dict(get_char_counts(get_book_text())))

    print_display('./books/frankenstein.txt', word_count, sorted_char_list)

if __name__ == "__main__":
    main()