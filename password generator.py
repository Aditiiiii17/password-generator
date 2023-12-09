#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_password(number, name):
    # Function to calculate the sum of digits until a single digit is obtained
    def get_single_digit_sum(num):
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num

    # Check if the number is valid
    try:
        number = float(number)
    except ValueError:
        return "Invalid input"

    # Convert the number to scientific notation
    scientific_notation = "{:e}".format(number)

    # Extracting coefficient and exponent from scientific notation
    coefficient, exponent = scientific_notation.split('e')
    coefficient = float(coefficient)
    exponent = int(exponent)

    # Simplify digits after the decimal point to a single digit
    coefficient_sum = get_single_digit_sum(int(coefficient * 10**(-exponent)))

    # Create S1 by concatenating the first three letters of each digit
    S1 = ''.join([str(coefficient_sum)[:3] for digit in str(coefficient_sum).replace(".", "")])

    # If the digit resulting from reducing the exponent to a single digit is odd, create S2
    if exponent < 0:
        exponent_sum = get_single_digit_sum(abs(exponent))
        if exponent_sum % 2 == 1:
            S2 = ''.join([name[i - 1] for i in range(1, len(name) + 1, 2)])
        else:
            S2 = ''

    # If exponent is zero or positive, S2 is an empty string
    else:
        S2 = ''

    # Combine S1 and S2 with "@" symbol
    password = S1 + "@" + S2

    return password


# Input the number of test cases
T = int(input("Enter the number of test cases: "))

for _ in range(T):
    # Input the number and name for each test case
    number, name = input().split()

    # Get and print the password for the current test case
    result = get_password(number, name)
    print(result)


# In[ ]:




