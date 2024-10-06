import unittest

class LoginSystem:
    def __init__(self):
        self.correct_username = "user123"
        self.correct_password = "pass123"
    
    def login(self, username, password):
        """Checks if the username and password are correct."""
        if username == self.correct_username and password == self.correct_password:
            return "Login successful"
        else:
            return "Login failed"
    
    def prompt_user_login(self): 
        """Prompts the user to enter their login credentials."""
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        result = self.login(username, password)
        print(result)
        return result

if __name__ == '__main__':
    login_system = LoginSystem()  # Create an instance of LoginSystem
    while True: # When user enter correct credentials, the loop breaks
        if login_system.prompt_user_login() == "Login successful":
            print("You have successfully logged in!")
            break