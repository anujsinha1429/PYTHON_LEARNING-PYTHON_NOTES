def login_required(func):
    def wrapper(user):
        if not user.get("logged_in"):
            print("User must be logged in to access this function.")
            return 
        return func(user)
    return wrapper

@login_required
def view_dashboard(user):
    print("Welcome to your dashboard")

view_dashboard({"logged_in": True})  # Output: Welcome to your dashboard
view_dashboard({"logged_in": False}) # Output: User must be logged in to access this function.

