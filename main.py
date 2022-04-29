#!/usr/bin/env python3

import math

def countDigits(num):
    # Prevent domain error
    if num == 0:
        return 0
    else:
        return math.floor(math.log10(num)) + 1

# Get the first digit from the left
def getFirstDigit(num):
    return math.floor(num / (10**(countDigits(num)-1)))

# Recursive function to return a list of digits in a number
def getDigits(num, digits=[ ]):
    firstDigit = getFirstDigit(num)
    digits.append(firstDigit)
    digitCount = countDigits(num)
    remainingNum = num-(firstDigit*10**(countDigits(num)-1))
    remainingNumCount = countDigits(remainingNum)

    # Account for any zeroes in between
    if remainingNumCount != digitCount-1:
        digits = digits + [0]*((digitCount-1)-remainingNumCount)

    if remainingNum == 0:
        return digits
    else:
        # number without the first digit
        return getDigits(remainingNum, digits)


def findClosestRearrangement(digits, index=-1):
    # if current number is greater than the one to the left, swap them
    if index*-1 == len(digits):
        return -1
    if digits[index] > digits[index-1]:
        # if the current number is less than the one the left, switch them
        digits[index], digits[index-1] = digits[index-1], digits[index]
        # return the list of digits, but with the remaining digits sorted
        if index == -1:
            return digits
        else:
            firstHalf = digits[0:index]
            secondHalf = digits[index:]
            secondHalf.sort()
            return firstHalf + secondHalf
    else:
        return findClosestRearrangement(digits, index-1)

num = input("number: ")
digits = getDigits(int(num))
answer = findClosestRearrangement(digits)
digitsAsStrings = [ str(i) for i in answer ]
formattedAnswer = "".join(digitsAsStrings)
print(formattedAnswer)
