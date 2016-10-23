import sys


# TODO Should think of better iterations. logical iterations.

def main():

	for c in range(1,1000):
		for b in range(1,1000):
			for a in range(1,1000):
				if a+b+c == 1000 and a*a + b*b == c*c:
					print(a,b,c)
					print(a*b*c)
					sys.exit()



if __name__ == '__main__':
	main()
