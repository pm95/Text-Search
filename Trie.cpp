// Author: Pietro Malky
// Date: 09/25/2020
// Purpose: Node-based trie for efficient text search
// ToDo's: reduce computational overhead when constructing initial Trie
// compilation command: g++ --std=c++11  Trie.cpp -o trie && ./trie

#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Trie
{
    char value;
    vector<Trie> children;

    bool _add_node(Trie node)
    {
        for (Trie child : children)
            if (child.value == node.value)
                return false;
        children.push_back(node);
        return true;
    }

    void _add_word(string word, int w, vector<Trie> children, int i)
    {
        if (w >= word.length())
            return;

        char _char = word[w];

        // if main list of children nodes is empty, add first node to lists
        if (children.size() == 0)
        {
            Trie t(_char);
            children.push_back(t);
            return _add_word(
                word,
                w + 1,
                children[0].children,
                0);
        }

        // otherwise, traverse existing nodes until you find a matching one, or none
        else
        {
            while (i < children.size())
            {
                Trie node = children.at(i);

                // current node and char are the same
                if (node.value == _char)
                    return _add_word(
                        word,
                        w + 1,
                        node.children,
                        0);
                i++;
            }

            Trie t(_char);
            children.push_back(t);
            return _add_word(
                word,
                w + 1,
                children.at(children.size() - 1).children,
                0);
        }
    }

public:
    Trie(char value = '*')
    {
        this->value = value;
    }

    void print_value()
    {
        cout << this->value << endl;
    }

    void add_word(string word)
    {
        _add_word(
            word,
            0,
            children,
            0);
    }
};

int main()
{
    Trie t;
    t.add_word("hola");
    t.print_value();

    return 0;
}