from stats import count_word, count_char
import sys
def dict_to_list_of_dict(char_words):
    needed_list= []
    for char,num in char_words.items():
        if char.isalpha():
            needed_list.append({"char": char, "num": num})
    return needed_list

def check_input():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_words = count_word(sys.argv[1])
    print(f"Found {num_words} total words")
    char_words= count_char(sys.argv[1])
    other_ones= dict_to_list_of_dict(char_words)
    other_ones.sort(reverse= True, key=lambda d:d["num"])
    for items in other_ones:
        char= items["char"]
        num= items["num"]   
        print(f"{char}: {num}")
    print("============= END ===============")
if __name__ == "__main__":
    check_input()
    main()        