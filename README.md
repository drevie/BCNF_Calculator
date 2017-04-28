Daniel Revie
4/26/17
Data Management HW 6

The following is a program to compute the BCNF decomposition of a pair (relation, functional dependencies)


Required Classes: 
1. S - A stack of relations with methods:
	a. S.push(R) --> push a relatoin into the stack
	b. S.pop() ---> pop a relation from the stack
	c. S.isEmpty() --> returns true if the stack is empty

2. R - A relation is a set of attributes and can be implemented using an array of integers with valeus 0 	or 1. A[i] = 1 implies that the attribute with ASCII i is in the relation

3. F - A functional dependency

4. DB - Contains BCNF Decomposition of original relation



To calculate the closure of a function depdency we are using the following theorems:
1. Reflexivity If Y issubset X then X -> Y

2. Augmentation If X -> Y => in Z issubset R XZ -> YZ

3. Transitivity If X -> Y and Y -> Z => X -> Z

-Special note, the rhs() function of a FD only implementes Axioms 1 and 3. To make sure it is robust we must add Axiom B.  