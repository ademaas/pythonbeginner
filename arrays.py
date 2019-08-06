def twodimentional_array(x,y):
    bigarr=  [[[] for j in range(y)] for i in range(x) ]   

    for i in range(x):
        for j in range(y):
            bigarr[i][j]= i*j

    print(bigarr)
    

def main():
    print(' \n')
    value = input('please enter comma separated values for x and y: ')
    value = value.split(',')
    x= int(value[0])
    y= int(value[1])

    twodimentional_array(x,y)


main()


