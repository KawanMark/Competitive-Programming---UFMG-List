# https://judge.beecrowd.com/pt/problems/view/2653

joias = set()

try:
    while True:
        joia = input()
        joias.add(joia)
except EOFError:
    pass

print(len(joias))


# C++
#include <iostream>
#include <string>
#include <set>
#using namespace std;

#int main(){
#    set <string> tipos;
#    string joias;

#    while (cin >> joias){
#        tipos.insert(joias);
#    }
#    cout << tipos.size() << endl;
#    return 0;
#}

