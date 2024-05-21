#include <iostream>
using namespace std;

int main() {
  /*int myNum = 15;  // myNum is 15
myNum = 10;  // Now myNum is 10
cout << myNum;  // Outputs 10
this also works*/
    int myNum = 15;               // Integer (whole number without decimals)
    double myFloatNum = 5.99;    // Floating point number (with decimals)
    char myLetter = 'D';         // Character
    string myText = "Hello";     // String (text)
    bool myBoolean = true;       // Boolean (true or false)
    
    cout << myNum;
    cout << "\n";
    cout << myFloatNum;
    cout << "\n";
    cout << myLetter;
    cout << "\n";
    cout << myText;
    cout << "\n";
    cout << myBoolean;
    cout << "\n";

    int myAge = 35;
    cout << "I am " << myAge << " years old.";
    cout << "\n";

    int x = 5;
    int y = 6;
    int sum = x + y;
    cout << sum;
    
    return 0;
}