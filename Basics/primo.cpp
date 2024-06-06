//https://br.spoj.com/problems/PRIMO/

#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {

  long n;
  cin >> n;

  if (n <= 1) {
    cout << "nao" << endl;
    return 0;
  }
  if (n == 2) {
    cout << "sim" << endl;
    return 0;
  }
  if (n % 2 == 0) {
    cout << "nao" << endl;
    return 0;
  }

  bool isPrimo = true;

  for (long i = 3; i * i <= n; i += 2) {
    if (n % i == 0) {
      isPrimo = false;
      break;
    }
  }

  if (isPrimo) {
    cout << "sim" << endl;
  } else {
    cout << "nao" << endl;
  }

  return 0;
}
