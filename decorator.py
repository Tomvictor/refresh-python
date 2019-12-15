


# def smart_divide(func):
#    def inner(a,b):
#       print("I am going to divide",a,"and",b)
#       if b == 0:
#          print("Whoops! cannot divide")
#          return

#       return func(a,b)
#    return inner

def smart_divide(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner

@smart_divide
def divide(a,b):
    return a/b

print(divide(1,5))