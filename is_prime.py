import sys

def main():
	args = sys.argv
	
	if len(args) == 1:
		print('Argument not passed. Please check again')
		sys.exit()
	number = int(args[1])
	if is_prime(number):
		print("Number is prime.")
	else:
		print("Not a prime.")

def is_prime(number):
	if is_even(number):
		return False
	else:
		for i in range(3,number/2 + 1,2):
			if number % i == 0:
				return False
		return True

def is_even(num):
	if num % 2 == 0:
		return True
	else:
		return False

if __name__ == '__main__':
	main()	
		
 



