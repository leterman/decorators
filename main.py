from datetime import datetime
def logger(func):
    def inner1(*args, **kwars):
        result1 = func(*args, **kwars)
        data_log = datetime.now()
        date = data_log.strftime("%A-%d-%B %Y %I:%M:%S %p")
        name = r'C:\Users\Laterman\Documents\Python Projects\decorators\test.txt'

        with open(name, 'a', encoding="utf-8") as f:
            f.write(f'Имя функции: {func.__name__}\n{date}\nАргументы: {args}\nРезультат:{result1}\n')
            f.close()
    return inner1
@logger
def function_to_be_used(x,y):
    z = x + y
    return z
res = function_to_be_used(23, 21)