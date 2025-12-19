def get_word_count(blob=""):

    words = blob.split()
    word_count = len(words)

    return word_count

def get_char_counts(blob=""):
    char_dict = {}
    words = blob.split()
    
    for word in words:
        for char in word.lower():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1        

    return char_dict