from stats import count_words
import sys
def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    chars_dict = count_characters(text)
    chars_sorted_list = sort_list(chars_dict)
    #print(f"{num_words} words found in book")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"the'{item['char']}' character was found {item['count']} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(book):
    char_set = set()
    string = book.lower()
    char_list = list(string)
    list_dict = {}
    ordered_list = []
    for char in char_list:
        # print(char_list.count(char))
       if char not in char_set:
        char_set.add(char)
    for char in char_set:
        list_dict[char] = char_list.count(char)
        #print(char,list_dict[char])
        ordered_list.append([{"name":char,"count":int(list_dict[char])}])
    return list_dict

def sort_on(d):
    return d["count"]

def sort_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char":char,"count":dict[char]})
    sorted_list.sort(reverse=True,key=sort_on)
    return(sorted_list)
main()