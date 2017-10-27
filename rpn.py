#!/usr/bin/env python3
import operator
import readline
from colorama import init, Fore, Back, Style

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
			num_token = int(token)
			if num_token < 0:
				print(Fore.WHITE + Back.RED + token + Style.RESET_ALL, end=' ')
			else:
				print(Fore.RED + Back.WHITE + token + Style.RESET_ALL, end=' ')
		except ValueError:
			print(Fore.WHITE + Back.BLUE + token + Style.RESET_ALL, end=' ')
	print('=', end=' ')
	for token in arg.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = ops[token]
			result = function(arg1, arg2)
			stack.append(result)
	print(str(stack[0]))
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

# def function_without_a_test():
# 	a = 1
# 	b = 2
# 	c = 3
# 	d = a + b + c

if __name__ == '__main__': # __name__ stores the main thing being run
	# will not run if running from test_rpn.py
	main()