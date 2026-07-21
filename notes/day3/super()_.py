class user:
    def __init__(self,name):
        self.name=name


class admin(user):
    def __init__(self, name, level):
        super().__init__(name)  #calling parent class init, parent ka kaam parents seh hi karwao 
        self.level=level

a=admin("anuj",1)
print(a.name,a.level)

# output :anuj 1