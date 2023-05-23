

def find_longest_common_prefix(list_of_words):
    shortest_word = str(min(list_of_words, key=len))
    prefix = ""
    for i, char in enumerate(shortest_word):
        for word in list_of_words:
            if not word[i] == char:
                return prefix
        prefix += char
    return prefix

if __name__ == '__main__':
    array = ['anyhow', 'anyway', 'an', 'anything']  # largest common prefix is "an"
    print(find_longest_common_prefix(array))
    