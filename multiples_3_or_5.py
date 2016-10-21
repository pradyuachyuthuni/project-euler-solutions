import sys

args = sys.argv
if len(args) is 1:
	# print usage and exit
	sys.exit()


# obtaining multiples of 15

input_1 = int(args[1])
upper_limit = (input_1 / 15) + 1

multiples_of_15 = []

for i in range(1,upper_limit):
	multiples_of_15.append(15*i)

# obtaining multiples of 3

upper_limit = (input_1 / 3) + 1

multiples_3_or_5 = []

for i in range(1,upper_limit):
	multiples_3_or_5.append(3*i)


# obtaining multiples of 5

upper_limit = (input_1 / 5) + 1

for i in range(1,upper_limit):
	if 5*i not in multiples_of_15:
		multiples_3_or_5.append(5*i)

print(multiples_3_or_5)
