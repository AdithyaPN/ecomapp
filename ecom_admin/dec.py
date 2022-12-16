# decorators
# decorators are used for write new logic without change its existing logic

def div_dec(func):

    def wrapper(a,b):
        if b>a:
            a,b = b,a # swapping
        return func(a,b)
    return wrapper

@div_dec # decorator function calls to the logical function this way
def div(a,b):
    print(a/b)

div(5,10)
