# GraphConnectivity
A little class for quickly finding the connected components of a graph

Sample Input:

8 8

2 1

1 2

8 2

2 8

8 6

8 3

5 7

4 7

4 1


the first line indicates that we are answering questions about 8 nodes, and 8 edges between them
then follow each edge, i.e. edge from 2 to 1, then 1 to 2 etc. 

Assumes bidirectional edges

last line asks whether nodes 4 and 1 are connected. 

I believe this is a fairly fast implementation. I think it's linear in amortized time: O(nodes+edges)

We construct a Graph structure which holds a component for every node initially, then we collapse the nodes into 
singular components and alter the duplicates to references to the nodes containing a set of all connected nodes
When we travel the path of references to the node containing the component set, we update the references of all nodes 
traversed so as to point to the node containing the proper component, hopefully keeping the traversal shorter in the
long run. 


Problems:

This is for a course, and I believe I edited the class to reindex the node values in a range from 0 to however many nodes there are -1
Then the edges are swapped back 1 as well, so as to be compatible. 
(The course provides input indexed starting at 1. -_-)

Similarly, there is some redundancy with edges and node indexing in build_components
This doesn't really impact performance, but harms readability, and is just unnecessary. 
