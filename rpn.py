#!/usr/bin/env python3

def calculate(arg):
	stack = list()
	for token in arg.split():
		if token == '+':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
		elif token == '-':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg2 - arg1
			stack.append(result)
		else:
			stack.append(int(token))
	# print(stack)
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__': # __name__ stores the main thing being run
	# will not run if running from test_rpn.py
	main()