def get_word_count(file_contents):
    word_count = 0
    words_in_text = file_contents.split()
    for word in words_in_text:
        word_count += 1
    return word_count

def get_character_count(file_contents):
    
    num_of_characters = {}
    lowercased = file_contents.lower()
    for character in lowercased:
        if character in num_of_characters:
            num_of_characters[character] += 1
        else:
            num_of_characters[character] = 1
    return num_of_characters

def sort_list(dict):
    list_of_dicionaries = []
    for character, count in dict.items():
        if character.isalpha():
            single_dict = {character: count}
            list_of_dicionaries.append(single_dict)
    list_of_dicionaries.sort(reverse=True, key=lambda x: list(x.values())[0])
    return list_of_dicionaries


