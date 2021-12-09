
#include<stdio.h>
struct Node
{
    int data;
    struct Node *next;
};
//------------------------push() for insertion-----------------------
void push(struct Node** head, int data)
{
    struct Node* p = (struct Node*)malloc(sizeof(struct Node));
    p->data = data;
    p->next = *head;
    *head = p;
}
// Time Complexity :- O(1)