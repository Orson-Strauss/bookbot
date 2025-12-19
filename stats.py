def get_word_count(blob: str):

    words = blob.split()
    word_count = len(words)

    return word_count

def get_char_counts(blob: str):
    char_dict = {}
    words = blob.split()
    
    for word in words:
        for char in word.lower():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1        

    return char_dict

def sort_on(item):
    return item["num"]

def sort_char_dict(char_dict):
    sorted_char_list = []

    for key in char_dict:
        if key.isalpha():
            sorted_char_list.append(
                {
                    "char": key, 
                    "num" : char_dict[key]
                }
            )
    
    sorted_char_list.sort(reverse=True, key=sort_on)
    
    return sorted_char_list