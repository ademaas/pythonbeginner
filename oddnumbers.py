#Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.

def listoddnumber(number):
    value = []
    list =[x for x in number.split(',')]
    for i in list:
        s= str(i)
        if int(s)%2!=0:
            value.append(s)

    print(','.join(value))

def main():

    number = input('Provide the input number: ')

    listoddnumber(number)


if __name__=="__main__":

    main()

