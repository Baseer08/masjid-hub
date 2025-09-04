class User:
    """Creating user profiles"""
    def __init__(self, f_name, l_name, email, ID):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.ID = ID

    def describe_user(self):
        print(f"{self.f_name} {self.l_name} is a user with an email {self.email} and ID is {self.ID}")

    def greet_user(self):
        print(f"Good Morning! {self.f_name} {self.l_name}")


users = User("Baseer", "Mohammed", "mdbaseer@hmail.com", "123")

users.describe_user()
users.greet_user()