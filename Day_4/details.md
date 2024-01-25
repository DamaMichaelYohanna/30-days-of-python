# Queue Data structure
A __Queue__ is a linear data structure which follows the 
**First-In-First-Out(FIFO)** principles. More like joining a line to be served in a pizza store or going to the bank to use
the ATM. In __Queue__ elements are added at the tail while they are being removed from the head.
For smooth addition and subtraction of Node, Each node will have a reference to the one behind it. 

Queue has majorly three operations: 
- enqueue(insert a new node at the tail of the queue)
- dequeue(remove the node at the head)
- size(length of the Queue)

To implement Queue successfully, we need to first of all have nodes which
will hold the data and the reference
to the next node in the sequence. 

The contained python files are a simple implementation of a __Queue__ data structure and a simple test to check the 
few functionality added.