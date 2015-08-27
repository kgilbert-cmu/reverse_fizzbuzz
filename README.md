# Reverse Fizz Buzz

Submission for [Daily Programming # 229 Intermediate](https://www.reddit.com/r/dailyprogrammer/comments/3iimw3/20150826_challenge_229_intermediate_reverse_fizz/).

It's too slow, though.

	~/programming/daily/229 $ time python main.py -f 2-5-4.txt -v yes
	BFS depth: 0
	BFS depth: 1
	BFS depth: 2
	BFS depth: 3
	BFS depth: 4
	BFS depth: 5
	BFS depth: 6
	BFS depth: 7
	BFS depth: 8
	[2, 5, 4]

	real	0m0.069s
	user	0m0.054s
	sys	0m0.013s

	~/programming/daily/229 $ time python main.py -f 3-5.txt -v yes
	BFS depth: 0
	BFS depth: 1
	BFS depth: 2
	BFS depth: 3
	BFS depth: 4
	BFS depth: 5
	BFS depth: 6
	[3, 5]

	real	0m0.043s
	user	0m0.028s
	sys	0m0.012s

	~/programming/daily/229 $ time python main.py -f 3-1-8-8-2.txt -v yes
	BFS depth: 0
	BFS depth: 1
	BFS depth: 2
	BFS depth: 3
	BFS depth: 4
	BFS depth: 5
	BFS depth: 6
	BFS depth: 7
	BFS depth: 8
	BFS depth: 9
	BFS depth: 10
	BFS depth: 11
	BFS depth: 12
	BFS depth: 13
	BFS depth: 14
	BFS depth: 15
	BFS depth: 16
	BFS depth: 17
	[3, 1, 8, 8, 2]

	real	1m18.296s
	user	1m17.704s
	sys	0m0.232s

	~/programming/daily/229 $ time python main.py -f 6-9-10-11.txt -v yes
	BFS depth: 0
	BFS depth: 1
	BFS depth: 2
	BFS depth: 3
	BFS depth: 4
	BFS depth: 5
	BFS depth: 6
	BFS depth: 7
	BFS depth: 8
	BFS depth: 9
	BFS depth: 10
	BFS depth: 11
	BFS depth: 12
	BFS depth: 13
	BFS depth: 14
	BFS depth: 15
	BFS depth: 16
	BFS depth: 17
	BFS depth: 18
	BFS depth: 19
	BFS depth: 20
	BFS depth: 21
	BFS depth: 22
	BFS depth: 23
	BFS depth: 24
	BFS depth: 25
	BFS depth: 26
	BFS depth: 27
	BFS depth: 28
	BFS depth: 29
	BFS depth: 30
	BFS depth: 31
	BFS depth: 32
	[6, 9, 10, 11]

	real	1m33.627s
	user	1m32.306s
	sys	0m0.425s
