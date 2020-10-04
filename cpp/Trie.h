// Author: Pietro Malky
// Date: 09/25/2020
// Purpose: Node-based trie for efficient text search
// ToDo's: reduce computational overhead when constructing initial Trie
// compilation command: g++ --std=c++11  Trie.cpp -o trie && ./trie

#ifndef TRIE_H
#define TRIE_H

#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Trie
{
    char value;
    vector<Trie> children;

    bool _add_node(Trie node);

    string _generate_trie(int level);

    void _add_word(string word, int w, vector<Trie> &_children);

    bool _search_word(string word, int w, vector<Trie> &_children);

public:
    Trie();

    Trie(char value);

    void print_value();

    void print_trie();

    void add_word(string word);

    bool search_word(string word);
};

#endif