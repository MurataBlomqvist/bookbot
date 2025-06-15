from stats import get_num_words
from stats import get_book_text
from stats import get_char_count
from stats import sort_dict_char_count
import sys

first_header = "============ BOOKBOT ============"
second_header = "----------- Word Count ----------"
third_header = "--------- Character Count -------"
fourth_header = "============= END ==============="

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    str_text_content = get_book_text(file_path)

    int_num_words = get_num_words(str_text_content)
    dict_char_count = get_char_count(str_text_content)
    sorted_dict_char_count = sort_dict_char_count(dict_char_count)
    
    print(first_header)
    print(f"Analyzing book found at {file_path}")
    print(second_header)
    print(f"Found {int_num_words} total words")
    print(third_header)
    for entry in sorted_dict_char_count:
        if entry["char"].isalpha():
            print(entry["char"] + ": " + str(entry["count"]))

    print(fourth_header)
    

main()
