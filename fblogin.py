import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://m.facebook.com'

# Directory where login data can be saved or retrieved
output_directory = 'D:\data'  # Change this to the appropriate directory

# Create a list to store all opened browser windows
open_windows = []


def banner():
    os.system('clear')
    _ = "-" * 44
    ban = f"""
    {_}
    _     ____  _____ _  _     
    / \   /  300/user/
    | |   | / \|| |  _| || |\ ||
    | |_/\| \_/|| |_//| || | \||
    \____/\____/\____\\\\_/\_/  \|
    [Author : ROCKFORT X KARINA ]
    [Github : https://github.com/Rockfort73 ]
    {_}
    """
    print(ban)


def perform_login(user, pswd):
    try:
        # Initialize the WebDriver for the new window
        driver = webdriver.Chrome()

        # Open the Facebook login page
        driver.get(url)

        # Find the username and password input fields and submit button using different locators
        username_field = driver.find_element(By.XPATH, "//input[@name='email' or @name='email']")
        password_field = driver.find_element(By.XPATH, "//input[@name='pass']")
        login_button = driver.find_element(By.XPATH, "//button[@name='login']")

        # Enter the username and password
        username_field.send_keys(user)
        password_field.send_keys(pswd)

        # Click the login button
        login_button.click()

        # Wait for a while to ensure the login process completes
        driver.implicitly_wait(10)

        # Check if the login was successful (you can change this condition based on your needs)
        if 'login' not in driver.current_url:
            print(f'\n   [\033[38;5;83mSuccessfully Log In!\033[0m] \033[0m\n\n')
            open_windows.append(driver)
        else:
            sys.exit("\033[38;5;208mIncorrect details\033[0m")

    except Exception as e:
        print(e)
        sys.exit('An error occurred during the login process')


def login_new():
    banner()
    user = input('[✦] //Username or Email//: ')
    pswd = input('[✦] //Password//: ')

    perform_login(user, pswd)
    save_login_data(user, pswd)


def login_saved():
    banner()
    # Check if login data file exists
    login_data_file = os.path.join(output_directory, 'login.txt')
    if not os.path.exists(login_data_file):
        sys.exit("\033[38;5;208mNo saved login data found\033[0m")

    # Read all login data from the file
    with open(login_data_file, 'r') as file:
        lines = file.readlines()
        login_data = []
        user = None
        for line in lines:
            if line.startswith("Username/Email: "):
                user = line.split(": ")[1].strip()
            elif line.startswith("Password: "):
                pswd = line.split(": ")[1].strip()
                if user and pswd:
                    login_data.append((user, pswd))

    for user, pswd in login_data:
        perform_login(user, pswd)


def close_all_windows():
    for window in open_windows:
        window.quit()
    open_windows.clear()


def save_login_data(user, pswd):
    login_data_file = os.path.join(output_directory, 'login.txt')
    with open(login_data_file, 'a') as file:
        file.write(f'Username/Email: {user}\n')
        file.write(f'Password: {pswd}\n')


if __name__ == "__main__":
    while True:
        print("[1] Login with new credentials")
        print("[2] Login with saved credentials")
        print("[3] Close all windows")
        print("[4] Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            login_new()
        elif choice == "2":
            login_saved()
        elif choice == "3":
            close_all_windows()
        elif choice == "4":
            sys.exit("hallo karina!")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
2