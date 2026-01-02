def count_book_words(book_text_as_string):
    
    words = book_text_as_string.split()
    
    return len(words)

def count_book_characters(book_text_as_string):
    
    character_dictionary = {}
    
    for c in book_text_as_string.lower():
        
        if c not in character_dictionary:
            character_dictionary[c] = 1
        else:
            character_dictionary[c] += 1

    return character_dictionary

def ordered_book_characters(unordered_char_dictionary):

    def sort_on(items):
        return items["num"]

    sorted_list = []
    
    for key in unordered_char_dictionary:
       
        expanded_dict = {}
        
        expanded_dict["char"] = key
        expanded_dict["num"] = unordered_char_dictionary[key]
        
        sorted_list.append(expanded_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list
