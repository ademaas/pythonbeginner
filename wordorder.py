def word_order(input_word):     

    sorteditem = input_word.sort()

    print(','.join(sorteditem))

def main():

    input_word = [x for x in input('Please provide a comma separated sentences: ').split(',')]

    input_word.sort()
    print(','.join(input_word))
    print('here is the sentence in alpahabetical order \n')


if __name__ == "__main__":
    main()

  
