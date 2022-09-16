from Decorator import decorator
from make_trace import make_trace
from make_log import make_log


# @decorator('log_div.txt')  # div = decorator(div)
@make_log('log_sum_make_log.txt')
def div(a, b):
    return a / b


# @decorator('log_sum.txt')   # summator = decorator(summator) # если баз @
# @make_trace('log_sum_make_trace.txt')
@make_log('log_sum_make_log.txt')
def summator(a, b, c):
    return a + b + c


if __name__ == '__main__':

    # summator = decorator(summator) # если баз @
    # div = decorator(div)
    print(summator(1,2,3))
    for i in range(10):
        print(summator(2, 10, c=i))
        print(div(i, 2))