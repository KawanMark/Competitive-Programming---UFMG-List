//https://vjudge.net/problem/CodeForces-1203C


#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    ll arr[n];
    for(int i = 0; i < n; ++i){
        cin >> arr[i];
    }

    ll mdc = arr[0];
    for(int i = 1; i < n; ++i){
        mdc = __gcd(mdc, arr[i]);
    }

    int numDiv = 0;
    for(ll i = 1; i * i <= mdc; ++i){
        if(mdc % i == 0){
            numDiv +=2;

            if(i *  i == mdc){
                numDiv--;
            }
        }
    }

    cout << numDiv << endl;


    return 0;
}
