#include<stdio.h>
#include<string.h>


void function() {
char buffer1[5];
scanf("%s",buffer1);
int *ret;
ret = buffer1 + sizeof(char)*21;
(*ret) += 7;
}

void main() {
int x,y;
x = 0;
function();
x = 1;
printf("%d\n",x);
}
