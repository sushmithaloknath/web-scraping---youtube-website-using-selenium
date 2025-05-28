# YouTube Trending Videos Scraper with Selenium

This Python script automates the extraction of the top trending YouTube videos' titles and view counts using Selenium WebDriver.

---

## Features

- Opens YouTube Trending page
- Extracts video titles and view counts for the top 20 trending videos
- Handles exceptions during data extraction gracefully
- Prints the results to the console
- Closes the browser automatically after completion

---

## Requirements

- Python 3.x
- Selenium
- Chrome browser
- ChromeDriver compatible with your Chrome version (make sure `chromedriver` is in your system PATH)

---

## Installation

1. Install Selenium via pip:
   ```bash
   pip install selenium
2. Download ChromeDriver and add it to your system PATH.

Usage
Clone this repository or download the script file.

Run the script:
python slyoutube.py

The script will open a Chrome browser window, load the YouTube Trending page, print the top 20 video titles and views in the console, then close the browser.
