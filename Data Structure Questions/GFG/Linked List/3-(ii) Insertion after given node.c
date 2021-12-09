#include<stdio.h>
struct Node
{
    int data;
    struct Node* next;
};

void insertAfter(struct Node* head, int data)
{
    struct Node *t=head,*p = (struct Node*)malloc(sizeof(struct Node));
    p->data = data;
    if(t==NULL)
        

}