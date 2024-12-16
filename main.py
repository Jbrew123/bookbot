def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = word_count(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(str(num_words) + " words found in the document")
        print("")
        char_count(file_contents)


def word_count(input_string):
    words = input_string.split()
    return len(words)


def char_count(contents):
    lower_contents = contents.lower()
    char_dict = {}
    for line in lower_contents:
        for character in line:
            if character in char_dict:
                char_dict[character] = char_dict[character] + 1
            else: 
                char_dict[character] = 1
    
    

    for entry in char_dict:
        if entry.isalpha():
            print("The "  + entry + " character was found " + str(char_dict[entry]) + " times")





main()