from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
import subprocess
import requests
import json
from decouple import config

# Function to send an SMS
def send_sms(recipient, message):
    url = config("URL")
    
    token = config("TOKEN")

    payload = json.dumps({
      "sender": config("SENDER_ID"),
      "recipient": recipient,
      "message": message,
      "call_back": config("YOUR_CALLBACK_URL_ADDRESS"), #If you do not have a callback URL you get one from webhook.site for free
      "bulk": 1
    })
    
    headers = {
      'Content-Type': 'application/json',
      'Authorization': token
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)



# Function to perform the voting actions
def perform_vote():
    # Initialize the WebDriver (you may need to specify the path to your WebDriver executable)
    driver = webdriver.Edge()  # Or webdriver.Firefox() for Firefox

    # Navigate to the website
    # website_url = "https://afrikamasharikitransportawards.com/login/" (Uncomment if you need to login directly without registering new user)
    website_url = "https://afrikamasharikitransportawards.com/"
    driver.get(website_url)

    # Fill out the login form (Uncomment appropriately upto line 57 if you have existing login details)
    # username = "Makey"
    # password = "Password1"

    # username_field = driver.find_element("id", "username-8929")
    # password_field = driver.find_element("id", "user_password-8929")

    # username_field.send_keys(username)
    # password_field.send_keys(password)

    # Submit the login form
    # login_button = driver.find_element("id", "um-submit-btn")
    # login_button.click()


    # Function to get random user data from the Ninja API
    def get_random_user():
        api_url = config("API_URL")
        headers = {'X-Api-Key': config("API_KEY")}
        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == requests.codes.ok:
                data = response.json()
                return data
            else:
                print(f"Error: Unable to fetch random user data. Status Code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    # Get random user data
    if (random_user := get_random_user()):
        pass
    # Check if random user data is available
    if random_user:
        username = random_user["username"]
        email = random_user["email"]

        # Fill out the registration form
        password = config("Password")
        confirm_password = config("Password")
        print(f"Username: {username}")
        print(f"Email: {email}")
    else:
        print("Random user data not available.")


    username_field = driver.find_element("id","user_login-8928")
    email_field = driver.find_element("id","user_email-8928")
    password_field = driver.find_element("id","user_password-8928")
    confirm_password_field = driver.find_element("id","confirm_user_password-8928")


    username_field.send_keys(username)
    email_field.send_keys(email)
    password_field.send_keys(password)
    confirm_password_field.send_keys(confirm_password)


    # Submit the registration form
    registration_button = driver.find_element("id","um-submit-btn")
    registration_button.click()

    # Wait for registration to complete (adjust the sleep time as needed)
    time.sleep(10)

    # Navigate to the voting page
    voting_page_url = "https://afrikamasharikitransportawards.com/vote-2/"
    driver.get(voting_page_url)

    # Scroll to the section with the voting options
    driver.execute_script("window.scrollTo(0, document.getElementById('polls-24').offsetTop);")

    form_id = "polls_form_24"
    form = driver.find_element("id", form_id)

    # Select your voting options (modify as needed)
    option1 = driver.find_element("id", "poll-answer-201")

    # Click the "Vote" button
    vote_button = driver.find_element("name", "vote")
    option1.click()

    # Check whether the radio button is selected
    is_selected = option1.is_selected()

    # Print the result
    print("Is the radio button selected?", is_selected)


    # Locate the div element by its ID
    div_id = "polls-24"
    # div_element = driver.find_element("id", div_id)

    # Locate the form by its ID
    form_id = "polls_form_24"
    form = driver.find_element("id",form_id)

    # Locate the "Vote" button within the form by its name and value attributes
    vote_button_xpath = ".//input[@name='vote' and @value='   VOTE   ']"
    vote_button = form.find_element(By.XPATH, vote_button_xpath)

    # # Submit your vote
    vote_button = driver.find_element(By.NAME, "vote")

    # Click the "Vote" button
    vote_button.click()

    time.sleep(20)

    # Locate the div element that contains the voting results by its ID
    results_div_id = "polls-24-ans"
    results_div = driver.find_element("id",results_div_id)

    # Extract and print the text content of the results div
    results_text = results_div.text
    print(results_text)


    # Locate all the <div> elements with class "pollbar"
    pollbar_elements = driver.find_elements(By.CSS_SELECTOR, 'div.pollbar')

    # Initialize a flag to check if you have voted
    voted_flag = False

    # Initialize a variable to store the voted result
    voted_result = ""


    # Locate all the <div> elements with class "pollbar"
    pollbar_elements = driver.find_elements(By.CSS_SELECTOR, 'div.pollbar')

    # Loop through each pollbar element and print its title attribute
    for pollbar in pollbar_elements:
        title_attribute = pollbar.get_attribute('title')
        print(f"Title Attribute: {title_attribute}")

    # Loop through each pollbar element and print its title attribute
    for pollbar in pollbar_elements:
        title_attribute = pollbar.get_attribute('title')
        
        if "You Have Voted For This Choice" in title_attribute:
            voted_flag = True
            voted_result = title_attribute
            print(f"Poll Result: {voted_result}")
        elif voted_flag:
            print(f"Poll Result: {title_attribute}")


    # Send an SMS for the voted result
    if voted_result:
        recipient = config("Phone_Number")  # Replace with the recipient's phone number
        message = f"Voted Result: {voted_result}"
        send_sms(recipient, message)

        # Close the browser
        time.sleep(10)
        driver.quit()

while True:
    print("Performing vote...")
    perform_vote()
    print("Waiting for 3 minutes before the next vote...")
    time.sleep(180)  # 900 seconds = 10 minutes