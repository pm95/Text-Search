from Trie import Trie

t = Trie()

# text_read_start, text_read_end, word_create_start, word_create_end = 0

with open("./shakespeare.txt", "r", newline="\n") as fin:
    text = fin.readlines()
    line: str
    for line in text:
        words = line.strip().split(' ')
        for word in words:
            t.add_word(word.lower())

while True:
    print(len(t.children))
    word = input("Enter a word to search in Shakespeare: ")
    word_found = t.search_word(word=word)
    print("was %s found? %s\n" % (word, word_found))
