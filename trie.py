# Author: Pietro Malky
# Date: 09/23/2020
# Purpose: Efficient trie-based text search algorithm

import os


class Node:
    def __init__(self, value: str = ""):
        super().__init__()
        self.children: list = []
        self.value = value

    def add_child(self, child: "Node") -> bool:
        c: Node
        for c in self.children:
            if c.value == child.value:
                return False
        self.children.append(child)

    def generate_trie(self) -> list:
        children_str: str = ""
        curr: str = ""

        c: Node
        for c in self.children:
            curr = c.value
            if len(c.children) > 0:
                curr = c.generate_trie()
            children_str += curr + ", "

        return "%s: [%s]" % (
            self.value,
            children_str
        )

    def print_self(self):
        print(self.value)

    def print_trie(self):
        print(self.generate_trie())


class TextSearcher:
    def __init__(self, path: str = ""):
        self.path: str = path
        self.text: str = ""
        self.first_chars: list = []

    def load_text(self):
        if self.path == "":
            self.text = ""
            return

        with open(self.path, "r") as fin:
            self.text = fin.read().lower()

    def print_text(self):
        print(self.text)

    def print_first_chars(self):
        char: Node
        for char in self.first_chars:
            char.print_trie()

    def extract_first_chars(self):
        result: list = []
        words: list = self.text.split(" ")
        for word in words:
            # modify these lines to improve runtime later on
            char_present = False
            c: Node
            for c in self.first_chars:
                if c.value == word[0]:
                    char_present = True
            if not char_present:
                self.first_chars.append(Node(word[0]))
        self.first_chars = self.first_chars

    def generate_trie(self):
        words: list = self.text.split(" ")
        for word in words:
            for char in word:
                print(char)


if __name__ == "__main__":
    t = TextSearcher("./data.txt")

    t.load_text()
    t.print_text()

    t.extract_first_chars()
    t.print_first_chars()

    # t.generate_trie()
