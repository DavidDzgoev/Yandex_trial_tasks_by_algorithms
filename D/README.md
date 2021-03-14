### D. Decrypt the cipher

| Time limit | Memory limit | Input                       | Output                        |
|------------|--------------|-----------------------------|-------------------------------|
| 9 sec      | 286Mb         | standard input or input.txt | standard output or output.txt |

Sherlock Holmes and Dr. Watson transmit encrypted messages consisting of numbers to each other. 
Each message is a square matrix *m × m*.
To decipher it, you need to get a sequence of numbers: print the values of the matrix in a spiral, 
starting from the central element - moving up and then clockwise.
Write a program for Holmes and Watson that will receive a sequence of numbers from encrypted messages.

### Input format
The first line contains a natural odd number *m*,
*1 ≤ m ≤ 1000*.
In each of the following *m* lines written *m* integers ranging from *-1000* to *1000*

### Output format
Output a sequence from *m^2* numbers obtained from the matrix according to the described spiral traversal algorithm.
