//https://judge.beecrowd.com/pt/problems/view/2653

#include <iostream>
#include <string>
#include <set>
#using namespace std;

int main(){
    set <string> tipos;
    string joias;

    while (cin >> joias){
        tipos.insert(joias);
    }
    cout << tipos.size() << endl;
    return 0;
}
