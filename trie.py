# Author: Pietro Malky
# Date: 09/23/2020
# Purpose: Efficient trie-based text search algorithm

import os


class Node:
    def __init__(self, value: str = ""):
        super().__init__()
        self.children: dict = {}
        self.value = value

    def add_child(self, child: str) -> None:
        print(child)

    def get_child(self, idx: int) -> "Node":
        return self.children[idx]

    def generate_trie(self) -> dict:
        children_str: str = ""
        curr: str = ""
        for curr in self.children:
            if len(self.children[curr]) > 0:
                curr = curr.generate_trie()
            children_str += curr + ", "

        return "%s: [%s]" % (
            self.value,
            children_str
        )

    def print_self(self):
        print(self.value)

    def print_trie(self):
        print(self.children)


class TrieTextSearcher:
    def __init__(self, path: str = ""):
        self.path: str = path
        self.text: str = ""
        self.trie: Node = Node("*")

    def load_text(self):
        if self.path == "":
            self.text = ""
            return

        with open(self.path, "r") as fin:
            self.text = fin.read().lower()

    def generate_sub_trie(self) -> Node:
        pass

    def generate_trie(self):
        words: list = self.text.split(" ")
        word: str
        for word in words:
            i: int
            self.trie.add_child(Node(word[0]))

    def print_text(self):
        print(self.text)

    def print_trie(self):
        self.trie.print_trie()


class Trie:
    def __init__(self):
        self.root: dict = {
            "h": {
                "e": {
                    "l": {
                        "l": {
                            "o": {}
                        }
                    }
                }
            }
        }

    def _add_word_reversed(self, rev_word: str, idx: int, trie: dict) -> dict:
        if idx == len(rev_word):
            return trie

        char: str = rev_word[idx]

        trie = {
            char: {
                **trie
            }
        }

        return self._add_word_reversed(
            rev_word=rev_word,
            idx=idx + 1,
            trie=trie
        )

    def _generate_word_trie(self, word: str) -> dict:
        word_trie: dict = self._add_word_reversed(
            rev_word=''.join(reversed(word)),
            idx=0,
            trie={}
        )

        return word_trie

    def _add_trie_to_root(self, word_trie: dict):
        # WORD TRIE
        # get keys of word trie
        wt_keys: list = list(word_trie.keys())

        # get first char in word trie keys
        wt_char: str = wt_keys[0]

        # ROOT TRIE
        # create copy of self.root
        root: dict = self.root

        # get keys from root dict
        rt_keys: list = list(root.keys())

        # get first char in root trie keys
        rt_char: str = rt_keys[0]

        # temporary root string
        temp_root: str = ""

        while len(wt_keys) != 0:
            # get first char in word trie keys
            wt_char = wt_keys[0]

            # get first char in root trie keys
            rt_char = rt_keys[0]

            # traverse one more layer in word trie
            word_trie: dict = word_trie[wt_char]

            # if char from word trie is present in root trie, reduce root dict by one layer
            if wt_char in root and temp_root == "":
                print("%s in root" % wt_char)
                root: dict = root[wt_char]

            # otherwise, add new trie node to root
            else:
                print("%s NOT in root" % wt_char)

                temp_root += wt_char
                root[wt_char] = temp_root

                print(temp_root)

            # calculate word trie keys
            wt_keys: list = list(word_trie.keys())

            print("\n")

        print(root)

    def add_word(self, word: str):
        word_trie: Trie = self._generate_word_trie(word)
        self._add_trie_to_root(word_trie=word_trie)


if __name__ == "__main__":
    t = Trie()
    t.add_word("hola")
