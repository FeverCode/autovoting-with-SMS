# Auto Voting with SMS Notification

This Python script automates the voting process on a website and sends an SMS notification for the specific result "You Have Voted For This Choice."

## Description

This script uses Selenium to automate the voting process on a website and monitors the poll results. When it detects that you have voted for a specific option, it sends an SMS notification with the voted result.

## Prerequisites

- Python 3.x
- Selenium library (`pip install selenium`)
- Requests library (`pip install requests`)
- WebDriver for your browser (e.g., Firefox WebDriver)

## Usage

1. Clone this repository to your local machine.

   ```bash
    git clone https://github.com/FeverCode/autovoting-with-SMS.git


2. Set up the virtual environment and install the required libraries.

   ```bash
   cd autovoting-with-SMS
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Create a .env file and add your enviroment variables appropriately


5. Configure the script:

    Replace *voting_page_url* with the URL of the voting page you want to automate.

    Set up the SMS sending parameters in the send_sms function.
    Currently using [Sema SMS](https://semasms.co.ke/login) as my provider. You will need to register with your Preferred SMS partner and follow their documentation to integrate appropriately the SMS sending function.

6. Run the script.

   ```bash
   python voting.py
   ```
7. Customization

   * You can customize the script by modifying the following:

    * Voting page URL
    SMS sending parameters (recipient, message, API URL, Authorization) if you decide to the *voting.py* script. 
    
    * The updated script *vote.py* does not incorprate registering for an account or sending SMS you can run the file if you do not require the mentioned parameters.

    * Make sure you obtain proper authorization to run the scripts on your chosen voting website.

8. Author

    [FeverCode](https://github.com/FeverCode)
## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.


