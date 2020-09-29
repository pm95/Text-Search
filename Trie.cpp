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

    void _add_word(string word, int w, vector<Trie> &_children)
    {
        if (w >= word.length())
            return;

        char _char = word[w];

        // if main list of children nodes is empty, add first node to lists
        if (_children.size() == 0)
        {
            Trie t(_char);
            _children.push_back(t);
            return _add_word(
                word,
                w + 1,
                _children[0].children);
        }

        // otherwise, traverse existing nodes until you find a matching one, or none
        else
        {
            int i = 0;
            while (i < _children.size())
            {
                // current node and char are the same
                if (_children.at(i).value == _char)
                {
                    return _add_word(
                        word,
                        w + 1,
                        _children.at(i).children);
                }
                i++;
            }

            Trie t(_char);
            _children.push_back(t);
            return _add_word(
                word,
                w + 1,
                _children.at(_children.size() - 1).children);
        }
    }

    string _generate_trie(int level)
    {
        string children_str = "";
        string curr = "";

        // recursively generate trie string
        for (Trie node : this->children)
        {
            if (children.size() > 0)
                curr = node._generate_trie(level + 1);
            children_str += curr;
        }

        // generate number of indentations
        string indents = "";
        for (int i = 0; i < level; i++)
            indents += "-";

        return "\n|" + indents + this->value + children_str;
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

    void print_trie()
    {
        cout << _generate_trie(0) << endl;
    }

    void add_word(string word)
    {
        _add_word(
            word,
            0,
            children);
    }
};

int main()
{
    Trie t;
    t.add_word("hola");
    t.add_word("horario");
    t.add_word("amigo");
    t.add_word("hace");
    t.add_word("arrivederchi");
    t.print_trie();
    return 0;
}