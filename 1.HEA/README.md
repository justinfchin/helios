# Huffman Encryption Algorithm

## Problem:
- (Logic reasoning)
In Huffman encoding algorithm (sort the symbols in order and merge the top
two symbols iteratively until only one node is left), prove that for two
symbols A and B with probabilities p(A) >= p(B), then the resultant
sequence according to Huffman encoding procedure, the length of symbol A
is no longer than that of symbol B.
 
## Answer:
- If p(A) = p(B), symbols A and B can be found in the same level. Meaning their sequences have the same length and differ only in the last bit. However, if more symbols with equal probability to A and B are part of the tree, any of those symbols might be found at lower levels. The sequence length for each symbol would depend on the way the symbols were sorted. 

Consider symbols A, B, C each with the same probability p. 

ABC produces the following tree:

			 (p + p + p)
			   /	  \
			  A       (p + p)
			         /       \
			        B         C

But we can also obtain this:

			(p + p + p)
			   /	  \
			  B      (p + p)
			     	/       \
			       A         C

In other words, the sequence length for symbols with the same probability might be larger than others.


- If p(A) > p(B), We prove by contradiction. Assume the resultant sequence for A is longer than the sequence of B. 

According to the Huffman Encoding algorithm, n symbols produce (n - 1) nodes when merging.  

 * Procedure to prove:
 
 Start by Induction on the number of symbols:
 
 Base Case: when n is 2, trivial
 
 Induction Hypothesis: Assume it works for a tree R which is optimal for (n-1) symbols
 
 Induction Step: Adding symbols x and y to the tree R and removing z, we get tree T (reconstruct tree with new symbols)
 		(btw z = x + y). Now a and b can take any form, any pair of symbols in T
		
		Case 1: 
		
		Case 2:
		
		Case 3:
		
