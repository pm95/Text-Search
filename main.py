from Trie import Trie
from time import time
import re

# Quick stats:
# 09/27/2020: loading 5MB of text into trie: 4.68 seconds


if __name__ == "__main__":
    t = Trie()
    text_path = "./data/lorem.txt"

    # load words in text into Trie
    with open(text_path, "r", newline="\n") as fin:
        print("Opening %s" % text_path)
        line: str
        text = fin.readlines()

        start_trie_load = time()
        # timing for loading words to Trie
        for i, line in enumerate(text):
            # replace all non-alphanumeric characters in string with empty str
            # generate list of words in line by splitting by space
            words = (re.sub(r"[^a-zA-Z0-9_ ]+", "", line)).split(' ')

            # iterate through each word in list and add to trie
            for word in words:
                t.add_word(word.lower())
        end_trie_load = time()

        print("Trie loading time: %s\n\n" % (
            end_trie_load - start_trie_load
        ))

        print("Finished loading %s\n" % text_path)

    t.save_trie_to_disk()

    # ask user for word to search
    while True:
        print("Number of unique beginning chars: %s" % len(t.children))
        word = input("Enter a word to search in Shakespeare: ")
        word_found = t.search_word(word=word)
        print("\twas %s found? %s\n" % (word, word_found))
