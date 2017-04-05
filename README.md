Ever felt devastated not being to solve a game? It happened to me and I decided to share this solver with those who are in the similar situation. This program is a simple solver for the word-brain mobile game. You need to download an english-words dictionary file to feed the program (I found this one which works fine https://github.com/dwyl/english-words).

Input:
	ALL-LETTERS,N1,N2,...

Output:
	All possible word tuples which can be the answer to the puzzle.

Sample:

	puzzle:
		L A B B
		
		R L T I
		
		E C I S
		
		M S C U
		
		----- ------- ----
	Input to the program:
		labbrltiecismscu,5,7,4

	Output:
                ['smell', 'biscuit', 'crab']
		['lrecl', 'biscuit', 'bams']
		['succi', 'stibble', 'marl']
		['scler', 'biscuit', 'balm'] 
