//------------------------Introduction--------------------------
/* Linked List
        - Linear data structure
        - Elements area not stored at a contigous location
        - Elements are linked using pointers.
*/

//----------------------Why Linked List--------------------------
/* Arrays has following limitations -
    1) The size of the arrays is fixed. Size can not be altered at runtime due to the risk of overwriting other data.
    2) Insertion/Deletion a new element in an array is expensive(existing element have to be shifted).
*/

//-------------------------Advantage------------------------------
//  1) Dynamic size that can change at runtime.
//  2) Ease of Insertion/Deletion

//--------------------------Drawbacks-----------------------------
/*
    1) Random access is not allowed.
    2) Extra memory space for a pointer is required for each elements.
    3) Not access friendly.
*/

//--------------------------Creating Node-----------------------------------
struct Node
{
    int data;
    struct Node* next;
};

//------------------------LL with 3 nodes-----------------------------------
#include <stdio.h>
#include <stdlib.h>
 
struct Node {
    int data;
    struct Node* next;
};
 
// This function prints contents of linked list starting from
// the given node
void printList(struct Node* n)
{
    while (n != NULL) {
        printf(" %d ", n->data);
        n = n->next;
    }
}
 
int main()
{
    struct Node* head = NULL;
    struct Node* second = NULL;
    struct Node* third = NULL;
 
    // allocate 3 nodes in the heap
    head = (struct Node*)malloc(sizeof(struct Node));
    second = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
 
    head->data = 1; // assign data in first node
    head->next = second; // Link first node with second
 
    second->data = 2; // assign data to second node
    second->next = third;
 
    third->data = 3; // assign data to third node
    third->next = NULL;
 
    printList(head);
 
    return 0;
}