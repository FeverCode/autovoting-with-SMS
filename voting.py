from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from decouple import config

#This updated script doesn't require logging in or registration and doesn't send SMS to the user, If you require
#such functions run vote.py script

def perform_vote():
    # Initialize the WebDriver (you may need to specify the path to your WebDriver executable)
    driver = webdriver.Firefox()  # Or webdriver.Firefox() for Firefox

    # Navigate to the website
    website_url = config("website_url")
    driver.get(website_url)

    # Wait for registration to complete (adjust the sleep time as needed)
    time.sleep(10)

    # Navigate to the voting page
    voting_page_url = config("voting_page_url")
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
    div_element = driver.find_element("id", div_id)

    # Locate the form by its ID
    form_id = "polls_form_24"
    form = driver.find_element("id",form_id)

    # Locate the "Vote" button within the form by its name and value attributes
    vote_button_xpath = ".//input[@name='vote' and @value='   VOTE   ']"
    vote_button = form.find_element(By.XPATH, vote_button_xpath)


    # Click the "Vote" button
    vote_button.click()

    time.sleep(15)

    # Locate the div element that contains the voting results by its ID
    results_div_id = "polls-24-ans"
    results_div = driver.find_element("id",results_div_id)

    # Extract and print the text content of the results div
    results_text = results_div.text
    print(results_text)


    # Locate all the <div> elements with class "pollbar"
    pollbar_elements = driver.find_elements(By.CSS_SELECTOR, 'div.pollbar')

    # Loop through each pollbar element and print its title attribute
    for pollbar in pollbar_elements:
        title_attribute = pollbar.get_attribute('title')
        print(f"Title Attribute: {title_attribute}")

    # Close the browser
    driver.quit()

while True:
    print("Performing vote...")
    perform_vote()
    print("Waiting for 2.5 minutes before the next vote...")
    time.sleep(150)  # 150 seconds = 2.5 minutes