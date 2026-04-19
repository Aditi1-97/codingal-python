# program to find all substrings of a string

def printSubstrings(string):

    length = len(string)

    for outer in range(0, length):
        for inner in range(outer + 1, length + 1):
            print(string[outer:inner])


text = input("Enter a string: ")

printSubstrings(text)