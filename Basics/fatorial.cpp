// https://neps.academy/br/course/introducao-a-programacao/lesson/fatorial

#include <iostream>
#include <string>
#include <cstdio>
#include <stdio.h>
#include <string.h>

using namespace std;

int fat(int x) {
	if (x == 0 || x == 1) {
		return 1;
	}
	else {
		return x * fat(x - 1);
	}
}


int main() {

	int n;
	scanf("%d", &n);
	cout << fat(n);




	return 0;


}
