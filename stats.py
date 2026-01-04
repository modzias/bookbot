
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_count(text):
    char_count = {}
    for char in text:
        char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return char_count

def get_sorted_list(dict):
    sorted_list = []
    for key in dict.keys():
        sorted_list.append({"char": key, "num": dict[key]})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list
