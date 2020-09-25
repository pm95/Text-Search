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

    def _add_trie_to_root(
        self,

        word_trie: dict,
        word_trie_keys: list,
        word_trie_key: str,

        root_trie: dict,
        root_trie_keys: list,
        root_trie_key: str,
    ) -> dict:
        if len(word_trie_keys) == 0:
            print("word_trie_keys length is zero")
            return root_trie

        # if keys are the same in word and root tries, reduce them by one level
        if word_trie_key in root_trie:
            new_word_trie: dict = word_trie[word_trie_key]
            new_word_trie_keys: list = list(new_word_trie.keys())
            new_word_trie_key: str = new_word_trie_keys[0]
            new_root_trie: dict = root_trie[word_trie_key]
            new_root_trie_keys: list = list(new_root_trie.keys())
            new_root_trie_key: str = new_root_trie_keys[0]

            return self._add_trie_to_root(
                word_trie=new_word_trie,
                word_trie_keys=new_word_trie_keys,
                word_trie_key=new_word_trie_key,
                root_trie=new_root_trie,
                root_trie_keys=new_root_trie_keys,
                root_trie_key=new_root_trie_key,
            )

        # if keys are not the same, add branch to trie
        else:
            print("word trie")
            print(word_trie)
            print(word_trie_keys)
            print(word_trie_key)
            print("\n")
            print("root trie")
            print(root_trie)
            print(root_trie_keys)
            print(root_trie_key)
            print("\n")
            print("\n")

            new_word_trie: dict = word_trie[word_trie_key]
            new_word_trie_keys: list = list(new_word_trie.keys())
            new_word_trie_key: str = new_word_trie_keys[0]

            new_root_trie: dict = {
                **root_trie,
                word_trie_key: {}
            }

            print(new_root_trie)

            # new_root_trie: dict = root_trie[word_trie_key]
            # new_root_trie_keys: list = list(root_trie.keys())
            # new_root_trie_key: str = new_root_trie_keys[0]

    def add_word(self, word: str):
        word_trie: dict = self._generate_word_trie(word)
        word_trie_keys: list = list(word_trie.keys())
        word_trie_key: str = word_trie_keys[0]
        root_trie: dict = self.root
        root_trie_keys: list = list(root_trie.keys())
        root_trie_key: str = root_trie_keys[0]

        self._add_trie_to_root(
            word_trie=word_trie,
            word_trie_keys=word_trie_keys,
            word_trie_key=word_trie_key,
            root_trie=root_trie,
            root_trie_keys=root_trie_keys,
            root_trie_key=root_trie_key,
        )


if __name__ == "__main__":
    t = Trie()
    t.add_word("hola")
