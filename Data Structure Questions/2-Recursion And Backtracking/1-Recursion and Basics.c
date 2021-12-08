//-----------------------Definition of Recursion----------------
/*
>> Any function which calls itself is called recursive.
>> A recursive method solves a problem by calling a copy of itself to work on a smaller problem. This is called recursion step.
>> 
*/
//-------------------------Process---------------------------
/*
>> It is important to ensure that the recursion terminates.
>> Each time the function calls itself with a slightly simpler version of the original problem.
>> The sequence of smaller problems must eventually converge on the base case.
*/
//--------------------------------Why Recursion-------------------------
/*
-> Recursion is a useful technique borrowed from mathematics.
-> Recursive code is generally shorter and easier to write than iterative code.
-> Recursion is most useful for tasks that can be defined in terms of similar subtaskd.
-> Example: sort, search, and traversal problems.
*/

//-------------------------Memory Visulization-------------------------------
/*
> Each recursive call makes a new copy of that method in memory. Once a method ends(i.e, return some data), the copy of that returning method is removed from memory.
> The recursive solution look simple but visulization and tracing takes time.
*/

//---------------------------Note---------------------------
/*
>> Two type case- Recursive case and Base case.
>> Every recursive function case must terminate at a base case.
>> Base Case:- At some point, the function encounters a subtask that it can without calling itself. This case, where the function deos not recur, is called the base case.
>> Recursive Case:- Where the function calls itself to perform a subrask, is reffered to as the Recursive case.
>> Generallly, iterative solutions are more efficient than recursive solutions[Due to overhead of function calls].
>> A recursive algorithm can be imlemented without recursive fuction calls using a stack, but it's usually more trouble than its worth. That means any problem that can be solved recusively can also be solved iteratively.
>> For some problems, there is no iterative algorithms.
>> Some problems are best sited for recursive solutions while others are not.
*/

//----------------------------------Examples------------------------------
/*
1- Fibonacci Series, Factorial
2- Merge Sort, Quick Sort
3- Binary Search
4- Tree Traversal, InOrder, PreOrder, PostOrder
5- Graph Traversal: DFS and BFS
6- Dynamic Programming Examples
7- Divide and Conquer Algorithms
8- Tower of Hanoi
9- Backtracking Algorithms
*/

//-------------------------Recursive vs Iterative------------------------------
/* Recursion:-
       >> Terminates when a base case is reached.
       >> Each recursive call requires extra space on the stack frame(memory).
       >> If we get infinite recursion, the program may run out of memory and result in stack overflow.
       >> Solutions to some problems are easier to formulate recursively.

   Iteration:-
       >> Terminates when a condition is proven to be false.
       >> Each iteration does not require extra space.
       >> An infinite loop could loop forever since there is no extra memory being created.
       >> Iterative solutions to a problem may not always be as obvious as a recursive solution.
*/