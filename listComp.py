#LIST COMPREHENSION

#1. Create a list comprehension that generates squares of numbers from 1 to 10.
def squares():
    square_list = [x**2 for x in range(1, 11)]
    print(f"The squares of numbers from 1 to 10 is {square_list}")


#2. Use list comprehension to filter out even numbers from a given list + curriculum exercise.
def even_num():
    num = [2,3,5,76,43,1243,15,15,2345,465,2,43,5,6,7,8]
    print([n for n in num if n%2==0 ])


#3. Write a list comprehension to extract the first letter of each word in a sentence.
def first_letter():
    sentence = input("Enter a random sentence:\n>> ")
    print([letter[0] for letter in sentence.split(" ")])


#4. Generate a list comprehension that creates a list of tuples containing numbers and their squares, for numbers from 1 to 5.
def numberAndSquares():
    num =[1,2,3,4,5]
    print([(n, n**2) for n in num  ])


#5. Use list comprehension to flatten a list of lists into a single list.
def flattenList():
    list1 = [ [1, 2], [3, 4 ,5] , [6, 7, 8], [9, 10, 11] ]
    print([ el for lst in list1 for el in lst])

    
func = [squares, even_num, first_letter, numberAndSquares, flattenList]

def main():
    while True:
        choice = int(input("1: Q1\n2: Q2\n3: Q3\n4: Q4\n5: Q5\n"))
        if choice > 0:
            func[choice-1]()
            
        else:
            exit()
if __name__ == "__main__":
    main()








