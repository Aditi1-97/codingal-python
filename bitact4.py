def powerOf8(number):

    count = 0

    if (number > 0 and (number & (number - 1)) == 0):

        # count position of set bit
        while(number > 1):
            number >>= 1
            count += 1

        if(count % 3 == 0):
            return True
        else:
            return False

    return False


number = int(input("Enter your number: "))

if(powerOf8(number)):
    print(number, 'is a power of 8')
else:
    print(number, 'is not a power of 8')