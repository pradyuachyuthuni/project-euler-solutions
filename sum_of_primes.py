# problem no. 10
# importing is_prime.py file. it's in git
import is_prime as ip
import sys

def main():

	# checking if arguments are passed
	args = sys.argv
	if len(args) == 1:
		print("Argument not passed.")
		sys.exit()

	# picking the argument
	upper_limit = int(args[1])
	
	# proper arguments or not ?
	if upper_limit <= 1:
		print('Enter proper arguments.')
		sys.exit()

	# initializing sum to be 2. took care of first prime number.
	sum_of_primes = 2

	# checking upper limit provided
	if upper_limit == 2:
		print(sum_of_primes)
		sys.exit()
	
	# generating a list of number with upper limit. generating only odd numbers.
	# because no poin in generating even numbers
	my_list = (x for x in xrange(3,upper_limit,2))

	# checking if it is a single number
	try:
		number = my_list.next()
	except StopIteration:
		print(sum_of_primes + upper_limit)
		sys.exit()
		
	while number < upper_limit:
		if ip.is_prime(number):
			sum_of_primes += number
		try:
			number = my_list.next()
		except StopIteration:
			break

	print(sum_of_primes)


if __name__ == '__main__':
	main()
