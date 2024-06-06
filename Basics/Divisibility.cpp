//https://codeforces.com/problemset/problem/1328/A

#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
  int t;
  cin >> t;
  while (t--) {
    long long x, y;
    cin >> x >> y;
    long long num = x % y;
    if (num == 0) {
      cout << 0 << endl;
    } else {
      cout << y - num << endl;
    }
  }

  return 0;
}
