# Python-Algorithms
Python: Implementation of different Algorithm for Beginners
		
		
		(This reposity is made for educaitonal purposes only. Some examples are copied from different open source resources.)


	"""In computer science or programming, sequential steps which are used to perform a task on computer is called an algorithm. In our 		daily life, step by step process of solving any problem is called an algorithm."""


Every Algorithm has following characteristics:

1. Complexity:
	Time Complexity (How much memory does it require)
	Space Complexity (How much time does it require)

2. Classification:
	Serial or Parallel
	Deterministic or Non-deterministic
	Exact or Approximate
	
3. Input and Output:
	What input a algorithm accept and what it provide in output.

	Common Algorithms:
1. Sorting Algorithms:
	It is used on unorder data to sort the data in ascending or descending order.

2. Search Algorithms:
	It is used when we have to find a specific data in a large data structure. for example, finding a sub string within a string.
	
3. Computational Algorithms:
	It is used to calculate another type of data when one set of data is given.

4. Collection Algorithms:
	It is used when we have to work with collection of data (Filtering unwanted data, count specific items, etc)

	There are ways to determine/understand the performance of an Algorithm. The simplest is measure how an algorithm respond to a data set 		and the	other is Big-O notaion.
	Big-O notaion classifies the performance of an algorithm according to data size (When data given as input increases of decreases). "O" 		indicates the order of operation, such as time scale to perform an operation. Big-O has terms like O(1), O(logn), O(n), O(n logn) and 		O(n^2) which represent constant time, logarithmic, linear time, log lonear and quadratic respectively.

If you are working with Algorithms, you also, often,  need #Data_Structures. Algorithms and data structures go hand in hand in programming. Most, if not all, algorithms are made to work with data and we need a space and form in which data is going to be stored. Here comes data structures. We have many types of data structures these are used to store and organize data in such a way that it can be processed by given algorithms efficiently. Different scenarios need different algorithms as well as different data structutes to perform a particular tas

Following are some most commonly used data structures.
	1. Arrays
	2. Linked Lists
	3. Stack
	4. Queues
	5. Trees
	6. Hash Tables

1. Arrays:
	
	"""An array is a collection of elements in which a key/index indentifies the position of particular element."""

	There are two types of two types of arrays:
	Time complexity of array for calculation of item index is O(1) and for insertion and deletion of element at end it is O(n).

2. Linked List:
	
	"""A linked list is a collection of linear data elements -called nodes- which contains data and a field which points to the next 		element in the list."""
	Each node contains data the applicaiton needs adn a pointer to the net element of the list. Linked list has the following main types:

	1. Singly Linked List
	2. Double Linked List

	It has many advantages over arrays as inseriton and deletion of elements are easy and fast. (An implementation of linked list in 		Python 	is attached in repo named: Python_linkedList.py)


3. Stack:
	Stack is a data structure which is based on Last in first out (LIFO) process. Stack supports two main operations PUSH and POP. The 		last push element is the first to pop. Push and Pop both are constant time operations in stack.
	Example of use of stack in daily life is Expression processing and Back Tracking.

4. Queue:
	Queue is used same as stack but it is based on First In First Out (FIFO) process. Queue support adding and removing data like stack 		but the main difference is in queue the first element entered in data is the first to be out. Same as stack adding and removing of 		data is queue is also constant time operations. Example of uses of queues are order processing and Massaging Apps.







