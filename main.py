import os
import string
import sys

# Deep copy lists to prevent modifying x in x_new = foo(x)
from copy import deepcopy
from optparse import OptionParser

VERBOSE = -1

def debug(message, verbosity):
	"""Print message if verbosity level is met.

	Verbosity levels:
	0 = Nothing
	1 = Important  (Errors and typical print messages)
	2 = Messages   (Warnings and program status)
	3 = Sanity     (more status and/or "did I get here yet?")
	4 = Everything (crazy!)
	"""
	global VERBOSE
	if VERBOSE >= verbosity:
		print message

def mapper(i, rules, default = "", symbols = string.letters):
	"""Generalized fizzbuzz algorithm.

		i : integer
		rules : list of divisors
		default : default string if i is not divisible by any rule
		symbols : the language of words to print "Fizz" and "Buzz"

	symbols will default to a-zA-Z using string.letters
	
	Returns the fizzbuzz string for integer i.
	"""
	if len(rules) > 26:
		raise IndexError("Too many rules.")
	output = ""
	for idx, div in enumerate(rules):
		if i % div == 0:
			output += symbols[idx]
	if output == "":
		output = default
	return output


def fizzer(i):
	"""Implement canonical FizzBuzz using mapper()"""
	return mapper(i, [3, 5], default = str(i), symbols = ["Fizz", "Buzz"])


def fizzbuzz(lst):
	"""Print the FizzBuzz of every integer in lst"""
	return [fizzer(i) for i in lst]


def print_input(integers, length, limit = None, start = 1, verbose = True):
	"""Print the generalized fizzbuzz for a sequence of divisors

		integers : sequence of divisors from Intermediate #229
		length : the number of non-empty lines to print
		limit : stop iteration after `limit` times (default: None)
		start : first integer to iterate from (default: 1)
		verbose : should this function print output?

	If verbose is set to False, then this will *return* fizzbuzz.
	"""
	count = 0
	ret = []
	i = start
	while count < length:
		if limit != None and i > limit:
			break
		fb = mapper(i, integers) 
		if fb != "":
			debug("Found a non-empty multiple at: " + str(i), 4)
			ret.append(fb)
			count += 1
		i += 1
	if not verbose:
		return ret


def maximal(prints):
	"""Scan a fizzbuzz sequence and find the largest variable."""
	biggest = ""
	for line in prints:
		for variable in line:
			if variable > biggest:
				biggest = variable
	return string.letters.index(biggest) + 1


def increment(number, base):
	"""Increment a LITTLE-ENDIAN number in base B"""
	# in a loop, we don't want x_new = increment(x) to modify x
	# (in the event x is a list and not a tuple)
	digits = deepcopy(number)
	i = 0
	added = False
	while i < len(digits):
		if digits[i] >= base:
			digits[i] = 0  # carry the 1...
			i += 1
		else:
			digits[i] += 1
			added = True
			break
	if added:
		return digits
	else:
		return None


def n_ary(digits, total):
	"""List all numbers in base B whose digits sum to less than B.

		digits : number of digits to fill
		total : the base B and the total digits should sum to

	Returns a list of n-digit numbers in base-b.
	Each number is a list of digits in little-endian.
	"""
	m = [0] * digits
	members = [m]
	while m != None:
		m_new = increment(m, total)
		if m_new != None and sum(m_new) <= total:
			members.append(m_new)
		m = m_new
	return members


def options(variables, distance):
	"""Generate all BFS neighbors within D distance of variables.

		variables : v \in Z^n with v_i representing one divisor
		distance : edit distance to consider

	The edit distance between nodes v and w is:

		\sum_i abs(v_i - w_i)

	That is to say, it is the number of +1 increments necessary.

	Given a maximum number of +1 increments to apply,
	Return a list of all w within D range of variables.
	"""
	v = variables
	n = len(v)
	edit = n_ary(n, distance)
	opt = [[v[i] + t[i] for i in xrange(0, n)] for t in edit]
	debug("There are " + str(len(opt)) + " neighbors within " + str(distance) + " distance.", 3)
	return opt
	

def brute(prints, limit = 1e3):
	"""Brute-force solution to Intermediate #229.

		prints : sequence of strings
		limit : stop iterating BFS after this many levels

	Returns None or a list of divisors which produce `prints`.
	"""
	global VERBOSE
	number_vars = maximal(prints)
	number_lines = len(prints)
	iterations = 0
	bfs = 1
	variables = [1] * number_vars
	attempts = 0
	best = 0
	closest = None
	index = 0
	debug("Detected " + str(number_vars) + " variables over " + str(number_lines) + " lines.", 2)
	while True:
		debug("", 2)
		debug("At least " + str(attempts) + " attempts have been made.", 2)
		debug("Generating possibilities with BFS depth " + str(bfs)+ "...", 2)
		if limit != None and iterations > limit:
			return None
		for possibility in options(variables, bfs):
			attempts += 1
			debug("", 4)
			debug("Now trying possibility #" + str(attempts) + ": " + str(possibility), 3)
			x = print_input(possibility, number_lines, verbose = False)
			if VERBOSE >= 4:
				debug("Actual\tAttempt\tEqual?", 4)
				for i in xrange(0, len(prints)):
					debug("\t".join([prints[i], x[i], str(prints[i] == x[i])]), 4)
			if x == prints:
				debug("", 1)
				debug("______________________________________", 1)
				debug("A solution was found after " + str(attempts) + " attempts.", 1)
				return possibility
			else:
				matches = sum([v == p for v, p in zip(x, prints)])
				if matches > best:
					best = matches
					closest = possibility
					index = attempts
		if VERBOSE >= 2:
			debug("The closest match has been possibility #" + str(index) + ": " + str(closest), 2)
			debug("It had " + str(best) + " of " + str(len(prints))  + " matches (" + str(round(100 * best / float(len(prints)), 1)) + "%).", 2)
		bfs += 1


def init_parser():
	parser = OptionParser()
	parser.add_option("-f", "--file", dest = "File", type = "string", help = "Input file")
	parser.add_option("-v", "--verbose", dest = "Verbose", type = "int", help = "Verbosity level")
	(options, args) = parser.parse_args()  # user input is stored in "options"
	return options

def main():
	options = init_parser()
	if options.File == None:
		print "Error: No input file was provided."
		sys.exit(1)
	else:
		if not os.path.isfile(options.File):
			raise IOError("Could not find input file.")
	global VERBOSE
	if options.Verbose == None:
		VERBOSE = 1
	else:
		VERBOSE = options.Verbose
	lines = []
	with open(options.File, 'r') as input_file:
		for line in input_file:
			lines.append(line.strip())
	debug(brute(lines), 1)

if __name__ == "__main__":
	main()

