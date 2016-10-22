
def square_of_sum():
	sum_n1 = 0
	for i in range(101):
		sum_n1 += i 
	sum_n1 = sum_n1 * sum_n1
	return sum_n1

def sum_of_squares():
	sum_n2 = 0
	for i in range(101):
		sum_n2 += i*i
	return sum_n2

def main():
	print(square_of_sum() - sum_of_squares())

if __name__ == '__main__':
	main()
