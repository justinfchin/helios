# Huffman Encryption Algorithm

## Problem:
- (Logic reasoning)
In Huffman encoding algorithm (sort the symbols in order and merge the top
two symbols iteratively until only one node is left), prove that for two
symbols A and B with probabilities p(A) >= p(B), then the resultant
sequence according to Huffman encoding procedure, the length of symbol A
is no longer than that of symbol B.
 
## Answer:
  - Precondition: 
    - An array of 2 symbols. 
  - Postcondition: 
    - Returns a node, which is the root of the tree, where all the symbols are in the tree, and the higher probability symbols are no longer than that of the lower probability symbols. 
  - Base: 
    - Given k = 2 symbols, trivial.
      - Let + denote merge
      - Scenario:
        - p(A) >= p(B)
          - A + B = new node D
            - A.length = B.length
            - D.length < A.length & B.length
          - So, A.length <= B.length holds
    - Given k = 3 symbols
      - Introduce symbol C
      - Scenarios:
        - p(C) >= p(A) >= p(B)
          - A + B = new node D
            - A.length = B.length
            - D.length < A.length & B.length
          - So, A.length <= B.length holds
        - p(A) >= p(C) >= p(B)
          - C + B = D
            - C.length = B.length
            - D.length < C.length & B.length
          - D + A = new node E
            - E.length < D.length & A.length
            - D.length = A.length
          - Since D.length < C.length & B.length, then A.length < C.length & B.length.
          - So, A.length <= B.length holds
        - p(A) >= p(B) >= p(C)
          - B + C = D
            - B.length = C.length
            - D.length < B.length & C.length
          - D + A = new node E
            - E.length < D.length & A.length
            - D.length = A.length
            - Since D.length < B.length & C.length, then A.length < B.length & C.length.
          - So, A.length <= B.length holds
  - Induction Hypothesis:
    - Assume A.length <= B.length holds for all 0 < k < n symbols.
  - Induction Step:
    - Show that A.length <= B.length holds for n symbols. The idea here is to split the tree into subtrees with k symbols. So, given tree T1 with n symbols, we can find subtrees on the left and right of T1 (T2, T3 respectively) where T2, T3 are subtrees with k symbols. By induction hypothesis, subtrees, T2, T3 hold the property. We do this going up the tree till T1’ is of k symbols.
  - Termination:
    - The algorithm will end since we keep merging our symbols till we have one node left. This node is the root of our tree. 

