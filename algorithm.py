def algorithm(number_init):

    number_binary = "1"

    number_conv = str(number_init)

    number_len = len(number_conv)

    print(number_len)

    count = 64

    if count + 32 <= number_init:

        number_binary += "1"

        print(number_binary)

        count += 32

        print(count)

    else:

        number_binary += "0"

        print(number_binary)

        print(count)

    if count + 16 <= number_init:

        number_binary += "1"

        print(number_binary)

        count += 16

        print(count)

    else:

        number_binary += "0"

        print(number_binary)

        print(count)

    if count + 8 <= number_init:

        number_binary += "1"

        print(number_binary)

        count += 8

        print(count)

    else:

        number_binary += "0"

        print(number_binary)

        print(count)

    if count + 4 <= number_init:

        number_binary += "1"

        print(number_binary)

        count += 4

        print(count)

    else:

        number_binary += "0"

        print(number_binary)

        print(count)

    if count + 2 <= number_init:

        number_binary += "1"

        print(number_binary)

        count += 2

        print(count)

    else:

        number_binary += "0"

        print(number_binary)

        print(count)

    if count + 1 <= number_init:

        number_binary += "1"

        print(number_binary)

        count += 1

        print(count)

    else:

        number_binary += "0"

        print(number_binary)

        print(count)

number_init = int(input("Please enter an integer: "))

algorithm(number_init)
