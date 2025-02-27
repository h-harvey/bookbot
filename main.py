def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(file_contents):
    word_count = 0
    words_in_text = file_contents.split()
    for word in words_in_text:
        word_count += 1
    return word_count

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(f"{get_word_count(file_contents)} words found in the document")


main()  