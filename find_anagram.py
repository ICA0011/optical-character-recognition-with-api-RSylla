

def find_anagrams(list_of_words):
    dict_of_words = dict(enumerate(list_of_words))
    dict_of_anagrams = {}
    for k, v in dict_of_words.items():
        word_normal_form = "".join(sorted(v))
        if word_normal_form in dict_of_anagrams:
            dict_of_anagrams[word_normal_form].insert(0, v)
        else:
            dict_of_anagrams[word_normal_form] = [v]
    return {k: v for (k, v) in dict_of_anagrams.items() if len(v) > 1}

if __name__ == '__main__':
    file = open("files/websted-dict.txt", "r", encoding="utf-8")

    with file as f:
        list_of_words = f.read().splitlines()

    anagrams = find_anagrams(list_of_words)
    for k, v in anagrams.items():
        print(f"{k}: {v}")
    print(len(anagrams.items()))
