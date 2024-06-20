//https://olimpiada.ic.unicamp.br/pratique/p2/2017/f1/botas/

#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {

	int casos;

	while (cin >> casos) {
		map<int, pair<int, int>> botas;
		for (int i = 0; i < casos; i++) {
			int numBotas;
			char peBota;

			cin >> numBotas >> peBota;
			if (peBota == 'D') {
				botas[numBotas].first++;
			}
			else {
				botas[numBotas].second++;
			}
		}

		int pair = 0;

		for (auto& bota : botas) {
			pair += min(bota.second.first, bota.second.second);
		}

		cout << pair << endl;

	}
}
