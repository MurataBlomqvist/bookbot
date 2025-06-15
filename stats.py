
def get_book_text(file_path):

    with open(file_path) as f:
        file_content = f.read()

    return file_content


def get_num_words(book_content):

    words = book_content.split()
    num_words = len(words)

    return num_words

def get_char_count(file_content):
    
    char_count = {}
    for char in file_content:
        char = char.lower()
        if char not in char_count:
            char_count.update({char : 1})
        else:
            char_count.update({char : char_count.get(char) + 1})

    return char_count

def sort_on(dict):
    return dict["count"]

def sort_dict_char_count(dict_char_count):
    
    sort_dict_list = [{"char": "", "count": 0}]
    for key in dict_char_count:
        sort_dict_list.append(dict(char = key, count = dict_char_count.get(key)))

    sort_dict_list.sort(reverse=True, key=sort_on)

    return sort_dict_list
    
