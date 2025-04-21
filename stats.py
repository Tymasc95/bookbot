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
        
    

        
            
        