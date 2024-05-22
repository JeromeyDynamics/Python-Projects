#include <iostream>

//namespace - provides a solution for preventing name conflicts
//in large projects. Each entity needs a unique name. A namespace 
//allows for identically named entities as long as the namespaces
//are different

namespace first {
    int x = 1;
}
namespace second {
    int x = 2;
}

int main() {
    //double quotes are just for strings and single quotes are just
    //for characters
    //takes the x variable from the first function and prints it
    std::cout << "first: " << first::x << "\n";

    //initializes the second function
    using namespace second;
    //prints the x variable taken from the second function that 
    //was initialized
    std::cout << "second: " << x << "\n";
    
    //initialized the namespace std objects and can be placed 
    //at the top
    using namespace std;
    string name = "Bus";
    cout << "Hello " << name << "\n";

    //initializes the fact that you will be using standard 
    //output (using std::cout)
    using std::cout;
    //initializes the fact that you will be using standard
    //string (using std::string)
    //(normally you have to put std:: infront of strings)
    using std::string;
    //both of these using std lines are a safer alternative to
    //using namespace standard (using namespace std)

    string whatIsBus = "bussy";
    cout << "Hello " << name << " you are " << whatIsBus << "\n";

    return 0;
}