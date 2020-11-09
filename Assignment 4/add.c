#include <stdio.h>

int add(int x, int y){
	return x+y;
}

int main(){
	int x=1, y=2, z;
	z=add(1,2);
	printf("%d\n", z);
	return 0;
}
