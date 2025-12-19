def get_book_text():
    
    with open('./books/frankenstein.txt') as f:
        book_blob = f.read()
    
    return book_blob

def get_word_count(blob=""):

    words = blob.split()
    word_count = len(words)

    return word_count

def main():

    num_words = get_word_count(get_book_text())
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()