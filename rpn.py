#!/usr/bin/env python3
import operator
import readline

ops = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod
}

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = ops[token]
			result = function(arg1, arg2)
			stack.append(result)
	print(stack)
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

def function_without_a_test():
	a = 1
	b = 2
	c = 3
	d = a + b + c

if __name__ == '__main__': # __name__ stores the main thing being run
	# will not run if running from test_rpn.py
	main()