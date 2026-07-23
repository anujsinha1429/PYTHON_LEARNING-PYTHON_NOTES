# using @ symbol for decorator

def decorator(func):
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper

@decorator # yehi line upar wali line k barabar h

def hello():
    print("hello")
hello() 

# important line 
# yehi hello=decorator(hello) krke hello() call krne k barabar h