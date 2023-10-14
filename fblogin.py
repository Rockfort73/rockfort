from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://m.facebook.com'

def perform_login(user, pswd):
    try:
        # Set up ChromeOptions for mobile emulation
        mobile_emulation = {
            "deviceName": "iPhone X"  # Ganti dengan perangkat seluler yang diinginkan
        }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        # Initialize the WebDriver for the new window with mobile emulation options
        driver = webdriver.Chrome(options=chrome_options)

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
            print('\nSuccessfully Log In!\n')
        else:
            sys.exit("Incorrect details")

    except Exception as e:
        print(e)
        sys.exit('An error occurred during the login process')

# (Kode lainnya tetap sama)

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
