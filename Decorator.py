from datetime import datetime

def decorator(file_name):
    def decorator_(old_function):
        def new_function(*args, **kwargs):
            data = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            function_name = f' Имя {old_function.__name__}'
            arguments = f'  Аргументы {args}_{kwargs}'
            result = old_function(*args, **kwargs)
            result_str = (f' результат {result} \n')
            with open (file_name, 'a' , encoding='UTF8') as f:
                f.write(data+function_name+arguments+result_str)
            return result
        return new_function
    return decorator_


