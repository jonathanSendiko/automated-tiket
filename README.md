# Web Automation Script of tiket.com

This is a Python Scripts using Selenium and Chrome Webdriver to automate unit testing of tiket.com from the landing page until payment method for flight bookings.

## Development Environment

OS: Windows 10
Screen Resolution: 1920x1080p
Development App: Visual Studio Code
Testing Browser: Chrome (Zoom 110%, notebook default zoom rate)
Packages:

- Python 3.9.4
- Selenium 3.141.0
- ChromeDriver

## Package Requirement

Python:

- Windows: [Python Release Python 3.9.6 | Python.org](https://www.python.org/downloads/release/python-396/)
- Linux:
  > sudo apt-get update
  > sudo apt-get install python3
- Mac OS:
  > brew install python

Selenium:

> pip install selenium

ChromeDriver (Choose according to your Chrome Version):
[Downloads - ChromeDriver - WebDriver for Chrome (google.com)](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## How to Run

The script could be simply run by typing

> python testing.py

## Assumptions

This script is made only to test all the functionality within the website of tiket.com to make a transaction. So, only the top or the most popular flights are chosen. It is also made within the assumption of being ran using a desktop without any manual interference for each iteration of the script.

The tested functionalities are the select input, the text input, the page navigation on the button onClick action and API post on button-click.
