class user:
    # items=[] #class attribute
    def __init__(self):
        self.items=[] #instance attribute ab jo chahiye output mai whi milega na ki sabka same

    def add_item(self,item):
        self.items.append(item)

c1=user()
c2=user()
c1.add_item("apple")
c2.add_item("banana")
print(c2.items)
print(c1.items)