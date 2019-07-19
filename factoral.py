def factoral(x):
    if(x==0):
        return 1

    return x*factoral(x-1)

def main():
    inp = int(input('Please enter the number to the factorial:'))
    
    value_fac = factoral(inp)
    print(value_fac)

main()