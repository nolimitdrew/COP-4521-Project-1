# Andrew Stade
# 1/20/2021
# afs18c
# The program in this file is the individual work of Andrew Stade.


def Insert(counter,string):
    palindromes[counter] = string;

counter = 0
palindromes = {}
print("Enter the strings: \n", end="")
while True:
    string = input("")
    if string == 'Done':
        break
    else:
        temp = string
        string = string.lower()
        string = string.replace(" ", "")
        rev = ''.join(reversed(string))
        if rev==string:
            counter = counter + 1
            Insert(counter,temp)
print("The palindromes are: ")
print(palindromes)