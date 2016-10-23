# importing is_prime.py file. its in git
import is_prime as ip
import sys

def main():
	prime_count = 1 # took care of 2.
	number = 3

	while prime_count != 10001:
		if ip.is_prime(number):
			prime_count += 1
		number += 2 
	
	if prime_count == 1:
		print(number -1)
		sys.exit()

	print(number - 2)

if __name__ == '__main__':
	main()
