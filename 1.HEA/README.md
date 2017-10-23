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

		
- If p(A) > p(B), we will induct on the number of symbols for the Huffman Encoding tree. We take into consideration that the Huffman Algorithm is a greedy algorithm and it guarantees an optimal tree. 

	Base Case: When n = 2, that means the Huffman tree has two leaves and the root. Both leaves have depth 1 and therefore, symbols
		   A and B have the same sequence length. Trivial case. 
		   
	Induction Hypothesis: Assume it works for a tree R1 with the set S1 which has symbols {s1,s2,s3,......,x,y} U {z} - {x,y}. 
			      Symbol z has probability p(z) = p(x) + p(y).Set S1 has n symbols, where each symbol has its own   		 		      probability. R is optimal and symbol A has a shorter or equal lenght sequence as symbol B. Symbols 
			      A and B can be any pair in S1 that satisfy the probability condition p(A) > p(B). 
	
	Induction Step: A new tree called R2 is created from R1, which has the symbol set S2 as (S1 U {x,y} - {z}). S2 has (n + 1)
			symbols. We will apply the Induction Hypothesis in the following scenarios.  
			
		Scenario 1: x and y are siblings, and x and y are symbols A and B respectively. Since siblings have the same
			sequence length we are done. The rest of the tree still holds by the Induction Hypothesis.
				
		Scenario 2: Symbol A has a lower depth than symbol B. This means A already has a shorter sequence. We are done.
			By the induction hypothesis, A and B can be any pair of symbols and therefore, they are in an optimal
				Huffman Tree. 
				
		Scenario 3: Symbol A has a higher depth than symbol B. We contradict this scenario to prove that Huffman Encoding
			greedy procedure was not used with the symbols. 
				
			Assume tree R2 is optimal in this scenario. That means it is optimal while A has a longer sequence than B
			and p(A) > p(B). 
				
			We define a cost function for the Huffman tree:
				
			COST(tree) = Sum(p(i)d(i)) , where p(i) is probability of i and d(i) is the depth of i. 
				
			If we find the cost of R2 we have:
				
			COST(R2) = p(s1)d(s1) + ... + p(B)d(B) + ... + p(A)d(A) + ... + p(sn)d(sn)
				
			With the assumption, we belive COST(R2) is the most minimum cost possible. To contradict that, we switch
			A and B in R2 to create the tree R3. We calculate the cost for R3.
				
			COST(R3) = p(s1)d(s1) + ... + p(A)d(A) + ... + p(B)d(B) + ... + p(sn)d(sn)
				
			The cost of R2 should be less than R3 since it is optimal.
				
			COST(R2) < COST(R3)
			p(B)d(B) +  p(A)d(A) <  p(A)d(A) + p(B)d(B)
				
			Looking at the inequalities, d(A) for R2 is heavier than d(A) for R3. This means the cost for R3 is less
			than the cost for R2. Which is a contradiction to the optimality of R2. 
				
			This scenario is impossible because of the greedy algorithm Huffman Enconding. 
			Therefore, only the above two scenarios are possible for optimal trees. 
				
	Therefore, we have proved that the Huffman Enconding algorithm works for any n > 2 symbols while still being optimal and keeping
	higher probability symbols with sequences shorter or equal to symbols with lower probablities. 
				
				
				
				
				
			
