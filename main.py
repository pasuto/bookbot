import sys
from stats import count_book_words, count_book_characters, ordered_book_characters

def get_book_text(file_path):
    with open(file_path) as file:
         return file.read()

def main():

    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    characters = count_book_characters(get_book_text(sys.argv[1]))
    
    print (f"Found {count_book_words(get_book_text(sys.argv[1]))} total words")
    
    ordered_list_of_dicts = (ordered_book_characters(characters))

    for i in range(0, len(ordered_list_of_dicts)):
        if ordered_list_of_dicts[i]["char"].isalpha() == False:
            continue
        else:
            print(f"{ordered_list_of_dicts[i]["char"]}: {ordered_list_of_dicts[i]["num"]}")
main()
