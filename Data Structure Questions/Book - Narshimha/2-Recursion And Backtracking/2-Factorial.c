//-----------------------Recursion Method---------------------------
#include<stdio.h>
int factorial(int n)
{
    if(n==1)
        return 1;
    else
        return n*factorial(n-1);
}

int main()
{
    int n,result;
    printf("Enter a Number:");
    scanf("%d",&n);
    result = factorial(n);
    printf("Factorial: %d",result);
    return 0;
}