import string
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

def print_input(integers, length):
	for i in xrange(1, length):
		fb = mapper(i, integers) 
        if fb != "":
			print fb
