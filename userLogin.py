import unittest

# Simple login function to be tested
def login(username, password):
    correct_username = "user123"
    correct_password = "pass123"
    
    if username == correct_username and password == correct_password:
        return "Login successful"
    else:
        return "Login failed"

def prompt_user_login():
    # Input user's username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Call the login function and display the result
    result = login(username, password)
    print(result)

if __name__ == '__main__':
    # Continuously prompt the user to login until they are successful
    while True:
        prompt_user_login()
        # Optionally, break the loop if login is successful
        if login(input("Enter your username: "), input("Enter your password: ")) == "Login successful":
            print("You have successfully logged in!")
            break