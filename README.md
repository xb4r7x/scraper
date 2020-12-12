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

Note on shipping configuration. The shipping type is currently hard-coded in the script because I was being lazy (sorry). I've set it to select ground shipping, but if you would like to select a different option modify line 65 with a different numerical valule. Options as of the time of this writting are (these options are dictated by the vancafe website and are subject to change. Inspect the element on the page for current information, or test the script with invalid credit card information to make sure it's doing what you want) :

1098 - In store pickup
701 - ground
703 - 3 day select
704 - 2 day
714 - Next Day air
1059 - USPS Priority Mail

## Slack Notifications
In order for slack notifications to work you'll have to create a slack app and configure a webhook on a channel in your own slack instance. Slack's documentation for completing these steps is pretty clear so I won't reitterate. If you would like to forgo this step, simply comment out or remove any reference to the "notify_slack" function from the script and those actions will be skipped.

Once you have a slack webhook URL add it to your config file.

## Disclaimer
This script is a functioning prototype. There's plenty of more work and other things that could have been done to make it better, but I only needed it to work once and only had a couple hours to write it.This script is posted as-is. Use at your own risk and never run any scripts you find on the internet without understanding what they're doing.
