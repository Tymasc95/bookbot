def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = {}
    for character in text:
        lowered = character.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def dict_sorter(dict):
    chars_list = []
    for char, count in dict.items():
        if char.isalpha():
            chars_list.append({"char": char, "count": count})
    chars_list.sort(key=lambda x: x["count"], reverse=True)
    return chars_list
        
        
    

        
            
        