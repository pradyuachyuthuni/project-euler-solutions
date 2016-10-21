import sys

def main():
        args = sys.argv
        if len(args) is 1:
            print("Usage : Please specify a range. For example\npython 3n_plus_1.py 10 20")
            sys.exit()

        input_1 = int(args[1])
        input_2 = int(args[2]) + 1
        max_length_of_series = 1

        for i in range(input_1,input_2):
                num = i
                length = 1
                while num is not 1:
                        if num % 2 is 0:
                                num = num / 2
                        else:
                                num = 3*num + 1
                        length += 1
                if length > max_length_of_series:
                        max_length_of_series = length

        print(max_length_of_series)

if __name__ == '__main__':
        main()
