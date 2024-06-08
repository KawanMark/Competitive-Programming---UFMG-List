//https://br.spoj.com/problems/QUERM/


#include <bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[]) {

  int n;
  int casos = 1;
  while (cin >> n && n != 0) {
    vector<int> ingressos(n);

    for (int i = 0; i < n; i++) {
      cin >> ingressos[i];
    }

    int premiado = 0;
    for (int i = 0; i < n; i++) {
      if (ingressos[i] == i + 1) {
        premiado = ingressos[i];
      }
    }

    cout << "Teste " << casos << endl;
    cout << premiado << endl;
    cout << endl;
    casos++;
  }
  return 0;
}
