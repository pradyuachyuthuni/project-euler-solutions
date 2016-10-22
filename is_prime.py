import sys

def main():
	args = sys.argv
	
	if len(args) == 1:
		print('Argument not passed. Please check again')
		sys.exit()
	number = int(args[1])
	is_prime(number)

def is_prime(number):
	if number == 2:
		print("Number is the only even prime.")
	elif is_even(number):
		print("Number is not prime, its composite.")
	else:
		for i in range(3,number/2,2):
			if number % i == 0:
				break
		print("Number is prime.")

def is_even(num):
	if num % 2 == 0:
		return True
	else:
		return False

if __name__ == '__main__':
	main()	
		
 



