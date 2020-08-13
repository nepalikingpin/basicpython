print('Binary to Decimal Conversion')

binaryinput = (input('Enter a binary number\t'))
n = len(binaryinput)
decimal = 0
for x in binaryinput:
    decimal = decimal + int(int(x)*(2**(n-1)))
    n = n-1
print('The decimal value is',decimal)