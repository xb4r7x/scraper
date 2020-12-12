# Heater Sniper

# Setup Instructions (mac):

## Install Selenium
`pip3 install selenium`

## Install BeautifulSoup
`pip3 install beautifulsoup4`

## Download Chrome Driver
Download the latest chrome driver for selenium. I wrote this for use on a mac laptop. See below. If you're running a different OS you'll need the right driver for your OS. This should be easily found via google. 
`wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_mac64.zip && unzip chromedriver_mac64.zip && rm chromedriver_mac64.zip && mv ./chromedriver /usr/local/bin`

## Configuration
The script needs to know a few things to function. Specifically it needs your personal information. Rename the example file to "config.py" and modify all of the values to match your own information. You may want to modify the permissions on the file so that the script can read it and nobody else. It would also be a good idea to remove your personal information from this file when you're done using the script.

## Slack Notifications
In order for slack notifications to work you'll have to create a slack app and configure a webhook on a channel in your own slack instance. Slack's documentation for completing these steps is pretty clear so I won't reitterate. If you would like to forgo this step, simply comment out or remove any reference to the "notify_slack" function from the script and those actions will be skipped.

Once you have a slack webhook URL add it to your config file.

## Disclaimer
This script is a functioning prototype. There's plenty of more work and other things that could have been done to make it better, but I only needed it to work once and only had a couple hours to write it.This script is posted as-is. Use at your own risk and never run any scripts you find on the internet without understanding what they're doing.
