import random



def generator():
    first3_nums = []
    last4_nums = []
    # input for the company and country (must be in numbers)
    prefix = str(input("Enter your country's prefix: ")) + " "
    company = str(input("Enter the company prefix: ")) + " "
    # creating the first 3 numbers of the phone number
    for i in range(3):
        numbers1 = random.randint(0, 9)
        first3_nums.append(numbers1)
    # creating the last 4 numbers of the phone number
    for i in range(4):
        numbers2 = random.randint(0, 9)
        last4_nums.append(numbers2)

    # out of the lists we create strings
    first3_nums = "".join(map(str, first3_nums)) + " "
    last4_nums = "".join(map(str, last4_nums)) + " "
    return prefix + company + first3_nums + last4_nums


print(generator())
