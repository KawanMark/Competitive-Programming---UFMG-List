//https://vjudge.net/problem/HackerRank-si-lcm-and-hcf


#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    while(t--){
        ll a, b;
        cin >> a >> b;
        
        //O LCM é o menor número inteiro positivo que é múltiplo comum de dois ou mais números.
        long long lcmm = (a*b)/__gcd(a,b);

        //maximo divisor comum
        long long mdc = __gcd(a,b);

        cout << lcmm << " " << mdc << endl;
    }


    return 0;
}
