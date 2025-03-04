def h(n: int) ->float:
    return n+1
print(h(0))  # h takes int type argument and returns as float

try:
    result = 2/0
except ZeroDivisionError:
    print("oh noooo")
finally:
    result = 1
print(result)
try:
    raise Exception("yeeeeee")
except Exception as error:
    print(error)