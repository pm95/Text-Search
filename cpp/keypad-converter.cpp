/*
Author: Pietro Malky
Date: 10/04/2020
Purpose: Telephone keypad text resolver
    * Like texting in old times, if you wanted to generate the letter 'B' you'd have to press the key for number 2, twice. 
    * If You wanted the letter 'Y', you needed to press the key for 0, 3 times
    * Therefore I devised an algorithm to take in a sequence of number, e.g. 7444338777666, and output it's corresponding string, in this case, "PIETRO"
    * I first wrote the algorithm in Python and later re-wrote in in C++ for more efficient runtime
    * The time complexity is O(N), w.r.t. the length of the original number sequence string. This time complexity neglects string appending overhead 
*/

#include <iostream>
using namespace std;

class KeypadConverter
{
    string _number;
    int _counts[10];
    char _letter_mappings[10][4];
    string _result;
    string _convert();

public:
    KeypadConverter();
    string convert_number(string &number);
};

KeypadConverter::KeypadConverter() : _result(""),
                                     _number(""),
                                     _counts{0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                                     _letter_mappings{
                                         /*0*/ {'@', '@', '@', '@'},
                                         /*1*/ {'@', '@', '@', '@'},
                                         /*2*/ {'A', 'B', 'C', '@'},
                                         /*3*/ {'D', 'E', 'F', '@'},
                                         /*4*/ {'G', 'H', 'I', '@'},
                                         /*5*/ {'J', 'K', 'L', '@'},
                                         /*6*/ {'M', 'N', 'O', '@'},
                                         /*7*/ {'P', 'Q', 'R', 'S'},
                                         /*8*/ {'T', 'U', 'V', '@'},
                                         /*9*/ {'W', 'X', 'Y', 'Z'}} {};

string KeypadConverter::_convert()
{
    const int len = _number.length();
    int *numbers = new int[len];

    // generate array of integers from original number string
    for (int i = 0; i < len; i++)
        numbers[i] = numbers[i] * 10 + (_number[i] - 48);

    int i = 0;
    int j = 0;

    while (1)
    {
        //  setup local indeces
        int _i = numbers[i];
        int _j = _counts[_i] - 1;

        //  check if j reached end of numbers array
        if (j == len)
        {
            _result += _letter_mappings[_i][_j];
            break;
        }

        if (_i == numbers[j])
        {
            _counts[_i] = (_counts[_i] + 1) % 4;
            j += 1;
        }
        else
        {
            _result += _letter_mappings[_i][_j];
            _counts[_i] = 0;
            i = j;
        }
    }

    delete[] numbers;
    return _result;
};

string KeypadConverter::convert_number(string &number)
{
    _result = "";
    _number = number;
    return _convert();
};

int main()
{
    string num = "7444338777666";

    KeypadConverter kpc;
    string result = kpc.convert_number(num);

    cout << "Number: " << num << endl;
    cout << "Result: " << result << endl;

    return 0;
}