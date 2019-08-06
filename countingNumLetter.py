#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:

def inputValue(sentence):
    items = [x for x in sentence]
    digits=[]
    letters=[]

    for i in items:
        s = str(i)
        if(s.isdigit()==True):
            digits.append(s)
        if(s.isalpha()==True):
            letters.append(s)

    print('THE NUMBER OF DIGITS: ',len(digits))
    print('THE NUMBER OF LETTERS:',len(letters))

def main():

    #print('Please provide a sentence\n')

    sentence = input('Please provide a sentence: ')

    inputValue(sentence)

if __name__=="__main__":

    main()



