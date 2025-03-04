def d1(func):
    def wrapper(*argc,**argv):
        print("D1")
        func(*argc,**argv)
    return wrapper

def d2(func):
    def wrapper(*argc,**argv):
        print("D2")
        func(*argc,**argv)
    return wrapper
# Apply the decorator to a function

@d1
@d2
def say_hello(name):
    print("Hello!",name)

# Call the decorated function
say_hello("Uday")