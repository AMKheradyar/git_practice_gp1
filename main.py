#AmirMohammad
def pow_of_two_numbers(first_num: int, second_num: int) -> int:
    if second_num < 0:
        raise ValueError("Exponent cannot be negative.")
    if second_num == 0:
        return 1
    else:
        return first_num * pow_of_two_numbers(first_num, second_num - 1)

#Example
print(pow_of_two_numbers(2, 3))

# Parnian


# def remain_of_two_numbers():
#     pass


# Mohammad


# def sum_of_two_numbers():
#     pass


# Mehdi

def sub_of_two_numbers(num1 : int|float , num2 : int|float ) -> int|float :
    if num1 > num2:
        sub = num1 - num2
        return round(sub, 5)
        # return sub
    raise ValueError("Please enter bigger number first🙏🏻")

#Example1
print(sub_of_two_numbers(12,7))
#Example2
print(sub_of_two_numbers(7,12))


# Farzin


# def div_of_two_numbers():
#     pass


# Parsa


# def multi_of_two_numbers():
#     pass
