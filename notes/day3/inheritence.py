class user():
    def login(self):
        print("logged in")

class admin(user):
    def delete_user(self):
        print("user deleted")


a=admin() #iss line ka mtlb admin class ka object bna rha hu jisme user class ke sare properties and methods bhi aa jayenge
a.login() #is line ka mtlb login method call karna
a.delete_user() #is line ka mtlb delete_user method call karna

# inheritance sirf tab jab child truly parent ke type ka ho
# jaise admin user ka type hai isliye admin user ke methods use kar sakta hai