# decorator= function jo dusre function ko modify krta h bina uske code ko change kiye

# fucntion as a argument

def call_func(func):
    func()
def hello():
    print("hello world")

call_func(hello)      

# output: hello world


def outer():
    def inner():
        print("inner function")
    inner()
# outer()
f=outer()


# now decorator fuction

def decorator(func):
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper

def say_hello():
    print("hello")

hello=decorator(say_hello) #yaha pai ab say_hello() ko call krne pai wrapper function call hoga
hello()    #kuch v variable bana skte ho yaha pai
   

