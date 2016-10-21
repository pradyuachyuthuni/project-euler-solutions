# string reversal can be learnt in this problem


#TODO 
# assumed initial palindrome value as 1.
# should think of a better alternative

def main():
	palindrome = 1
	for i in range(999,0,-1):
		for j in range(999,0,-1):
			if str(i*j) == str(i*j)[::-1]:
				if i*j > palindrome:
					palindrome = i*j

	print(palindrome)


if __name__ == '__main__':
	main()
