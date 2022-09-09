def make_trace(old_function):
    def new_function(*args, **kwargs):
        print(f'вызвана функция {old_function.__name__}')
        print(f'с аргументами {args} и {kwargs}')
        result = old_function(*args, **kwargs)
        print(f'Получили {result}')
        print('-'*120)
        print('\n')
        return result
    return new_function

@make_trace
def my_sum(*args,**kwargs):
  s=0
  for i in (args):
    s += i
  for j in kwargs.values():
    s += j
  # print (*args)
  # print (args)
  # # print (**kwargs)
  # print (kwargs)
  # print (s)
  return s

print(my_sum(5,7,9,a=9,k=9))