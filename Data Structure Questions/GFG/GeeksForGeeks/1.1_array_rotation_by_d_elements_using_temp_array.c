#include<stdio.h>
void printArray(int arr[], int n);
void leftRotate(int arr[], int d, int n);

int main()
{
    int n,i,d;
    printf("Enter size of array: ");
    scanf("%d",&n);
    int arr[n];
    printf("Enter array: ");
    for(i=0;i<n;i++)
        scanf("%d",&arr[i]);
    printf("Enter number of rotation: ");
    scanf("%d",&d);
    leftRotate(arr, d, n);
    return 0;
}

void leftRotate(int a[], int d, int n)
{
    int i,temp[n];
    for(i=0;i<d;i++)
    {
        temp[i]=a[i];
    }
    for(i=0;i<n-d;i++)
    {
        a[i]=a[i+d];
    }
    for(i=0;i<d;i++)
    {
        a[n-d+i]=temp[i];
    }
    printArray(a, n);
}

void printArray(int a[], int n)
{
    printf("Roated Array: ");
    for(int i=0;i<n;i++)
        printf("%d ",a[i]);
    printf("\nTime Complexity: O(n)\nAuxiliary space: o(d)");
}