def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def count_words(book_text):
    count = 0
    for word in book_text.split():
        count+=1
    return count

def count_characters(book_text):
    char_count = {}
    for char in book_text:
        lowered = char.lower()
        if lowered in char_count:
            char_count[lowered] +=1
        else:
            char_count[lowered] = 1 
    return char_count

def sort_on(char_count):
    return char_count["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list