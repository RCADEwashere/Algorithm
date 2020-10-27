# Decimal to Binary conversion algorithm v.0.0.1

import sys

def algorithm(number_init):

    number_binary = "1"
    
    count = 2

    while count <= number_init:

        count *= 2

    count /= 2

    count_two = count / 2


    while count_two >= 1:

        if count + count_two <= number_init:
        
            number_binary += "1"
        
            count = count + count_two 

            count_two /= 2

        else: 

            number_binary += "0"

            count_two /= 2

    print("Binary: 0b%s" % number_binary)

    sys.exit(0)

number_init = int(input("Number: "))

if number_init == 0:

    print("Binary: 0b0")

    sys.exit(0)

else:

    algorithm(number_init)