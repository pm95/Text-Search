from Trie import Trie
from time import time
import re

# Quick stats:
# 09/27/2020: loading 5MB of text into trie: 4.68 seconds


def trie_based_search():
    # trie-based search
    t = Trie()

    # load words in text into Trie
    with open(text_path, "r", newline="\n") as fin:
        print("Trie-based search for %s" % text_path)
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

    while True:
        print("Number of unique beginning chars: %s" % len(t.children))
        word = input("Enter a word to search in %s: " % text_path)
        search_start = time()
        word_found = t.search_word(word=word)
        search_end = time()
        print("\twas %s found? %s\n" % (word, word_found))
        print("\ttime for search: %d" % (search_end - search_start))


def brute_force_search():
    # brute force search
    with open(text_path, "r", newline="\n") as fin:
        print("Brute force search for %s" % text_path)

        text = fin.readlines()

        while True:
            target = input("Enter a word to search in %s: " % text_path)
            target_found = False

            line: str
            search_start = time()

            for i, line in enumerate(text):
                # replace all non-alphanumeric characters in string with empty str
                # generate list of words in line by splitting by space
                words = (re.sub(r"[^a-zA-Z0-9_ ]+", "", line)).split(' ')
                # iterate through each word in list
                for word in words:
                    break_loop = False
                    if len(word) == len(target):
                        if word[0] == target[0]:
                            t = 0
                            while target[t] == word[t]:
                                t += 1
                                if t == len(target) - 1:
                                    target_found = True
                                    break_loop = True
                                    break
                    if break_loop:
                        break
            search_end = time()

            print("time for search: %s\n\n" % (
                search_end - search_start
            ))

            print("\twas %s found? %s\n" % (target, target_found))


if __name__ == "__main__":
    text_path = "./data/shakespeare.txt"
