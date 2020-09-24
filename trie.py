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
        self.nodes: dict = {
            "ROOT": {}
        }

    def add_child(self, child: str):
        self.nodes["ROOT"][child] = {}

    def add_word(self, word: str, idx: int, trie: dict):
        # if idx == len(word):
        #     return trie

        char: str = word[idx]
        trie = {
            **trie,
            char: {}
        }

        print(char, trie)

        # return self.add_word(
        #     word=word,
        #     idx=idx + 1,
        #     trie=trie[word[idx]]
        # )

    def print(self):
        print(self.nodes)


if __name__ == "__main__":
    t = Trie()
    word_trie = t.add_word(
        word="hola",
        idx=0,
        trie={}
    )

    t.print()
    print(word_trie)

    # t = TrieTextSearcher("./data.txt")

    # t.load_text()
    # t.print_text()
    # t.generate_trie()
    # t.print_trie()
