# function to calculate the number that is odd occuring

def OddOccurring(arr):

    # initialize result
      res = 0

      # transverse the array
      for element in arr:
            # XOR with the result
            res = res^element

      return res

# initialize our array
arr = []

# take array size as input
n = int(input("Enter a number: "))

# take array element input
while(n):
     num = int(input("Enter number: "))
     arr.append(num)
     n-=1

print("\n\nOdd occurring number is: ", OddOccurring(arr))       