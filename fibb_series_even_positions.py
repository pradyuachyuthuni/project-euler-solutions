
def main():
	first_num = 1
	second_num = 2
	required_sum = 2

	next_num = generate_next_fibb_number(first_num,second_num)
	while next_num < 4000000:
		if next_num % 2 is 0:
			required_sum += next_num 
		first_num = second_num
		second_num = next_num
		next_num = generate_next_fibb_number(first_num,second_num)
	print(required_sum)

def generate_next_fibb_number(x,y):
	return x+y


if __name__ == '__main__':
	main()
