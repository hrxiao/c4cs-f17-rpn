#!/usr/bin/env python3
import operator

ops = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow
}

#dict(operator)???

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
			
		# if token == '+':
		# 	arg1 = stack.pop()
		# 	arg2 = stack.pop()
		# 	result = arg1 + arg2
		# 	stack.append(result)
		# elif token == "-":
		# 	arg1 = stack.pop()
		# 	arg2 = stack.pop()
		# 	result = arg2 - arg1
		# 	stack.append(result)
		# else:
	# print(stack)
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__': # __name__ stores the main thing being run
	# will not run if running from test_rpn.py
	main()