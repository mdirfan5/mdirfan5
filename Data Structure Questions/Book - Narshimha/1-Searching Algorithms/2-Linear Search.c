//------------------------Linear search Algorithm------------------------------
/*
Linear_Search(a,n,value)
1. set i=0
2. repeat step 3 until for(i=0;i<n;i++)
3. if a[i] == value
   return i
   go to step 5
   [End of if]
   [End of loop]
4. return -1
5. exit
*/

//----------------------------Code---Method 1-------------------------------
#include<stdio.h>
int Linear_Search(int a[],int n, int value)
{
    int i;
    for(i=0;i<n;i++)
    {
        if(a[i]==value)
            return i;
    }
    return -1;
}

//---------------------------Driver Code------------------------------
int main()
{
    int n,i;
    scanf("%d",&n);
    int a[n],value;
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    scanf("%d",&value);
    int result = Linear_Search(a,n,value);
    (result==-1)?printf("Value Not Present"):printf("Value present at index %d",result);
    return 0;
}


//---------------------Method 2-----by flag variable-------------------------
int Linear_search(int a[],int n, int value)
{
    int i,pos=-1;
    for(i=0;i<n;i++)
    {
        if(a[i]==value)
        {
            pos = i; 
        }
    }
    if(pos==i)
        return pos;
    else
        return pos;
}


/*
Linear Seach Aproach:
    > Start from leftmost element of array and one by one compare "value" with each element of array.
    > If "value" matches with an element, return that index.
    > If "value" doesn't match, return -1.
Time Complexity:
    Worst Case    O(n) --> When element present at index n
    Best Case:    O(1) --> When element present at index 0
    Average Case: O(n) --> In between present in array
*/


//-------------------Method 3 Improved Worst-case Complexity--------------------------
//------------------------------(Or say more efficient)---------------------------------
int linear_search(int a[],int n,int value)
{
    int left = 0, right = n-1;
    int position = -1;

    // Run loop from 0 to right
    for(left=0;left<=right;)
    {
        if(a[left]==value)
        {
            position = left;
            break;
        }
        if(a[right]==value)
        {
            position = right;
            break;
        }
        left++;
        right--;
    }
    if(position == -1)
        return -1;
    else
        return position;
}