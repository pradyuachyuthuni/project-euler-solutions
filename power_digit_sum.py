
def main():
	my_string = str(2**1000).strip('L')
	sum_of_digits = 0

	for character in my_string:
		sum_of_digits += int(character)

	print(sum_of_digits) 

if __name__ == '__main__':
	main()
