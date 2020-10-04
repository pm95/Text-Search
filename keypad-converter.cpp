#include <iostream>
#include <vector>
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
                                         {'@', '@', '@', '@'},
                                         {'@', '@', '@', '@'},
                                         {'A', 'B', 'C', '@'},
                                         {'D', 'E', 'F', '@'},
                                         {'G', 'H', 'I', '@'},
                                         {'J', 'K', 'L', '@'},
                                         {'M', 'N', 'O', '@'},
                                         {'P', 'Q', 'R', 'S'},
                                         {'T', 'U', 'V', '@'},
                                         {'W', 'X', 'Y', 'Z'}} {};

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
            _counts[_i] += 1;
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
    string num = "2223323";

    KeypadConverter kpc;
    string result = kpc.convert_number(num);

    cout << "Number: " << num << endl;
    cout << "Result: " << result << endl;

    return 0;
}