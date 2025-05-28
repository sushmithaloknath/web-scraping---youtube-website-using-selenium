from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()
url = "https://www.youtube.com/feed/trending"

# Open YouTube Trending page
driver.get(url)
time.sleep(5)  # Wait for page to load

# Extract video titles and views
videos = driver.find_elements(By.XPATH, '//ytd-video-renderer')

for i, video in enumerate(videos[:20]):  # Get top 10 trending videos
    try:
        title = video.find_element(By.ID, "video-title").text
        views = video.find_element(By.XPATH, './/span[contains(text(), "views")]').text
        print(f"{i+1}. {title} - {views}")
    except Exception as e:
        print(f"Error extracting data for video {i+1}: {e}")

# Close the browser
driver.quit()
