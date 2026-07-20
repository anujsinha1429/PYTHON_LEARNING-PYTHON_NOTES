class user:
    def __new__(cls,name): #object create krta hai , memory allocate krta hai
        print("creating object")
        return super().__new__(cls)
    
    def __init__(self, name): #value assign krta hai
        print("initializing object")
        self.name = name

u=user("anuj")
print(u.name)        