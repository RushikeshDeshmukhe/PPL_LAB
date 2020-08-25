/*





*/

#include<stdio.h>
void main(){
int i,j;
for(i=2;i<=100;i++){
j=2;
while(j<i){
if(i%j==0){
if(i==j){
printf("%d \n",i);
}
break;
}
else
{
j++;
}
}
}


}
