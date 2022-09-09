from Decorator import decorator


@decorator('log_div.txt')  # summator = decorator(summator) # если баз @
def div(a, b):
    return a / b


@decorator('log_sum.txt')  # div = decorator(div)
def summator(a, b, c):
    return a + b + c


if __name__ == '__main__':

    # summator = decorator(summator) # если баз @
    # div = decorator(div)
    for i in range(10):
        print(summator(2, 10, c=i))
        print(div(i, 2))