#include <iostream>
#include "Trie.h"

using namespace std;

// compilation command: g++ --std=c++11 main.cpp Trie.cpp

int main()
{
    Trie t;
    t.add_word("hola");
    t.add_word("horario");
    t.add_word("amigo");
    t.add_word("hace");
    t.add_word("arrivederchi");
    t.add_word("arrivederchi");
    t.add_word("arrivederchi");
    t.add_word("arrivederchi");
    t.print_trie();

    cout << t.search_word("dog") << " dog" << endl;
    cout << t.search_word("hola") << " hola" << endl;
    return 0;
}