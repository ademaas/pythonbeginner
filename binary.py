#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
def check_divisiblity(number):

    input_number = [x for x in number.split(',')]

    for num in input_number:
        intnum = int(num,2)
        if intnum % 5 == 0:
            print(num)

    

def main():
    number = input('please provide comma separated binary number: ')

    check_divisiblity(number)


if __name__=="__main__":
    main()
