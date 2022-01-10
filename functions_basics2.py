# Countdown - Create a function that accepts a number as an input.
def countdown(num):
    x = []
    for i in range(num + 1):
        x.append(num - i)
    return x
print(countdown(15))

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def printAndReturn(num):
    print(num[0])
    return(num[1])
print(printAndReturn([17,3]))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def firstPlusLength(arr):
    sum = arr[0] + len(arr)
    return sum
print(firstPlusLength([10,5,17,4,16]))

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value.
def valueGreaterThanSecond(list):
    newList = []
    count = 0
    if (len(list) <= 1):
        return False
    
    for i in range(len(list)):
        if(list[i] > list[1]):
            newList.append(list[i])
            count += 1
    return newList
print(valueGreaterThanSecond([5,5,41,6,0,10,64]))
            
# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def lengthAndValue(size, value):
    list = []
    for i in range(size):
        list.append(value)
    return list
print(lengthAndValue(55,77))