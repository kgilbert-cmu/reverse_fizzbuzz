def fizzer(i):
	string = ""
	if i % 3 == 0:
		string += "Fizz"
	if i % 5 == 0:
		string += "Buzz"
	if string == "":
		string = str(i)
	return string

def fizzbuzz(lst):
	return [fizzer(i) for i in lst]

def main(lst):
	for x in fizzubzz(lst):
		print x
