#DICTIONARY COMPREHENSION

#1. Create a dictionary comprehension that maps each letter in the alphabet to its corresponding ASCII value.
def alphaAscii():
    print({chr(key) : key for key in range(97,123) })


#2. Generate a dictionary comprehension to convert a list of tuples into a dictionary.
def tupleDictionary():
    tuple_list =[('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7), ('H', 8), ('I', 9), ('J', 10), ('K', 11), ('L', 12), ('M', 13), ('N', 14), ('O', 15), ('P', 16), ('Q', 17), ('R', 18), ('S', 19), ('T', 20), ('U', 21), ('V', 22), ('W', 23), ('X', 24), ('Y', 25), ('Z', 26)]
    print({ key : value for key, value in tuple_list })


#3. Write a dictionary comprehension to filter out items with values greater than 100 from an existing dictionary.
def greaterThan():
    existingDict ={ "hi" : 100, "bye" : 120, "hllo" : 192, "no": 60, "henlo": 315, "hello": 40, "hallo" : 12}
    print({ key: value for key,value in existingDict.items() if value < 100 })    


#4. Create a dictionary comprehension to count the frequency of each letter in a given string.
def stringFrequency():
    string = input("Enter a string\n>> ")
    print({ key : string.count(key) for key in string })


#5. Use dictionary comprehension to swap keys and values in an existing dictionary.
def swapKeyValues():
    dictionary = {'MQT': 98, 'Iix': 94, "Yxc": 69}
    print({key:value for value, key in dictionary.items()})

func = [alphaAscii, tupleDictionary, greaterThan, stringFrequency, swapKeyValues]

def main():
    while True:
        choice = int(input("1: Q1\n2: Q2\n3: Q3\n4: Q4\n5: Q5\n6: Q6\n"))
        if choice > 0:
            func[choice-1]()
            
        else:
            exit()
if __name__ == "__main__":
    main()
            
