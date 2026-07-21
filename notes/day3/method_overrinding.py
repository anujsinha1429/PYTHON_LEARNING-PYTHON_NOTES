class user:
    def role(self):
        return "user"
    
class admin(user):    
    def role(self):
        return "admin"

a=admin()
print(a.role())  #admin ka role call hoga kyuki method overriding ho rha    