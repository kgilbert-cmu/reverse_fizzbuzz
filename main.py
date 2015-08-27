import string
import copy
from optparse import OptionParser
import sys
import os

def mapper(i, rules, default = "", symbols = string.letters):
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
	return mapper(i, [3, 5], default = str(i), symbols = ["Fizz", "Buzz"])

def fizzbuzz(lst):
	return [fizzer(i) for i in lst]

def print_input(integers, length, limit = None, start = 1, verbose = True):
	count = 0
	ret = []
	i = start
	while count < length:
		if limit != None and i > limit:
			break
		fb = mapper(i, integers) 
		if fb != "":
			if verbose:
				print fb
			ret.append(fb)
			count += 1
		i += 1
	if not verbose:
		return ret

def maximal(prints):
	biggest = ""
	for line in prints:
		for variable in line:
			if variable > biggest:
				biggest = variable
	return string.letters.index(biggest) + 1

def increment(number, base):
	digits = copy.deepcopy(number)
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

# all numbers in base total with D digits and less than total
def n_ary(digits, total):
	members = []
	m = [0] * digits
	while m != None:
		m_new = increment(m, total)
		if m_new != None and sum(m_new) <= total:
			members.append(m_new)
		m = m_new
	return members

def options(variables, distance):
	n = len(variables)
	edit = n_ary(n, distance)
	opt = [ [variables[i] + t[i] for i in xrange(0, n)] for t in edit]
	return opt
	

def brute(prints, limit = 1e3, verbose = False):
	number_vars = maximal(prints)
	number_lines = len(prints)
	iterations = 0
	bfs = 0
	variables = [1] * number_vars
	if verbose:
		print "Detected " + str(number_vars) + " variables over " + str(number_lines) + " lines."
	while True:
		if verbose:
			print "BFS depth:", bfs
		if limit != None and iterations > limit:
			return None
		for possibility in options(variables, bfs):
			x = print_input(possibility, number_lines, verbose = False)
			if x == prints:
				return possibility
		bfs += 1

def init_parser():
	parser = OptionParser()
	parser.add_option("-f", "--file", dest = "File", type = "string", help = "Input file")
	parser.add_option("-v", "--verbose", dest = "Verbose", type = "string", help = "Verbosity level")
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
	if options.Verbose == None:
		verbose = False
	else:
		verbose = True
	lines = []
	with open(options.File, 'r') as input_file:
		for line in input_file:
			lines.append(line.strip())
	print brute(lines, verbose = verbose)

if __name__ == "__main__":
	main()

