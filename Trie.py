# Author: Pietro Malky
# Date: 09/25/2020
# Purpose: Node-based trie for efficient text search
# ToDo's: reduce computational overhead when constructing initial Trie


class Trie:
    def __init__(self, value: str = "*"):  # done
        super().__init__()
        self.value = value
        self.children: list = []

    # private methods

    def _add_node(self, node: "Trie") -> bool:  # done
        child: Trie
        for child in self.children:
            if child.value == node.value:
                return False
        self.children.append(node)

    def _generate_trie(self, level: int) -> str:
        children_str: str = ""
        curr: str
        for node in self.children:
            if len(self.children) > 0:
                curr = node._generate_trie(level+1)
            children_str += curr

        return "\n|%s%s%s" % (
            "-"*level,
            self.value,
            children_str,
        )

    def _add_word(self, word: str, w: int, children: list, i: int) -> list:  # done
        if w >= len(word):
            return

        char: str = word[w]

        # if main list of children nodes is empty, add first node to list
        if len(children) == 0:
            children.append(Trie(char))
            return self._add_word(
                word=word,
                w=w+1,
                children=children[0].children,
                i=0
            )

        # otherwise, traverse existing nodes until you find a matching one, or none
        else:
            while i < len(children):
                node: Trie = children[i]

                # current node and char are the same
                if node.value == char:
                    return self._add_word(
                        word=word,
                        w=w+1,
                        children=node.children,
                        i=0
                    )
                i += 1

            children.append(Trie(char))
            return self._add_word(
                word=word,
                w=w+1,
                children=children[len(children)-1].children,
                i=0
            )

    def _search_word(self, word: str, w: int, children: list) -> bool:
        if w >= len(word):
            return True

        i: int = 0
        while i < len(children):
            if word[w] == children[i].value:
                return self._search_word(
                    word=word,
                    w=w+1,
                    children=children[i].children
                )
            i += 1

        return False

    # public methods

    def search_word(self, word: str) -> bool:
        return self._search_word(
            word=word,
            w=0,
            children=self.children
        )

    def add_word(self, word: str):  # done
        self._add_word(word=word, w=0, children=self.children, i=0)

    def print(self):
        print(self._generate_trie(level=0))

    def print_root(self):
        node: Trie
        for node in self.children:
            print(node.value)

    def save_trie_to_disk(self, path="./trie.txt"):
        with open(path, "w") as fout:
            fout.write(self._generate_trie(0))
