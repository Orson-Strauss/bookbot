from stats import get_word_count, get_char_counts

def get_book_text():
    
    with open('./books/frankenstein.txt') as f:
        book_blob = f.read()
    
    return book_blob

def main():

    num_words = get_word_count(get_book_text())
    print(f"Found {num_words} total words")
    print(get_char_counts(get_book_text()))

if __name__ == "__main__":
    main()